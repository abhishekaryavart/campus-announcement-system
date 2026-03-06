import bcrypt
from database.mongo import get_db
from bson import ObjectId
import config
import datetime

def hash_password(plain_text_password):
    """
    Hashes a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    # Store as string for MongoDB
    return hashed.decode('utf-8')

def check_password(plain_text_password, hashed_password):
    """
    Checks a plain text password against a stored bcrypt hash.
    """
    try:
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode('utf-8')
        return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)
    except Exception:
        return False

def init_security():
    """
    Bootstraps the `system_users` collection.
    If the collection is empty, it reads the `.env` ADMIN and MAIN_USER credentials 
    and inserts them with securely hashed passwords.
    """
    db = get_db()
    
    # Check if system_users is already populated
    if db.system_users.count_documents({}) == 0:
        
        # Seed Super Admin
        admin_hash = hash_password(config.ADMIN_PASSWORD)
        db.system_users.insert_one({
            "username": config.ADMIN_USERNAME,
            "email": config.ADMIN_EMAIL,
            "name": "System Administrator",
            "password_hash": admin_hash,
            "role": "super_admin",
            "created_at": datetime.datetime.utcnow(),
            "status": "active"
        })
        
        # Seed Main User (Operator/Admin)
        operator_hash = hash_password(config.MAIN_USER_PASSWORD)
        db.system_users.insert_one({
            "username": config.MAIN_USER_USERNAME,
            "email": config.MAIN_USER_EMAIL,
            "name": "Main Operator",
            "password_hash": operator_hash,
            "role": "operator",
            "created_at": datetime.datetime.utcnow(),
            "status": "active"
        })
        print("[SECURITY] Bootstrapped system_users from .env credentials.")

def get_all_system_users():
    """Fetches all system staff members."""
    db = get_db()
    users = list(db.system_users.find().sort("created_at", -1))
    for u in users:
        u['_id'] = str(u['_id'])
    return users

def add_system_user(username, email, name, password, role):
    """Creates a new staff member with hashed password."""
    db = get_db()
    if db.system_users.find_one({"email": email.lower().strip()}):
        return False, "Email already exists."
    
    user = {
        "username": username.strip(),
        "email": email.lower().strip(),
        "name": name.strip(),
        "password_hash": hash_password(password),
        "role": role,
        "created_at": datetime.datetime.utcnow(),
        "status": "active"
    }
    db.system_users.insert_one(user)
    return True, None

def update_system_user(user_id, name, email, role):
    """Updates staff name, email, or role."""
    db = get_db()
    try:
        db.system_users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {
                "name": name.strip(),
                "email": email.lower().strip(),
                "role": role
            }}
        )
        return True, None
    except Exception as e:
        return False, str(e)

def delete_system_user(user_id):
    """Removes a staff member."""
    db = get_db()
    try:
        db.system_users.delete_one({"_id": ObjectId(user_id)})
        return True, None
    except Exception as e:
        return False, str(e)
