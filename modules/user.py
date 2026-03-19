from database.mongo import get_db
from bson import ObjectId
import datetime
import uuid
from email_validator import validate_email, EmailNotValidError


def get_all_users():
    db = get_db()
    users = list(db.users.find().sort("created_at", -1))
    for u in users:
        u['_id'] = str(u['_id'])
    return users


def get_user_by_id(user_id):
    db = get_db()
    try:
        user = db.users.find_one({"_id": ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
        return user
    except Exception:
        return None


def get_users_by_target(target_dict):
    """
    Resolve a targeting dictionary against the users collection.
    target_dict = {
        'target_type': 'all'|'student'|'faculty'|'alumni'|'department'|'course'|'year',
        'department': str,
        'course': str,
        'year': str
    }
    """
    db = get_db()
    query = {"status": "active"}

    t_type = target_dict.get('target_type', 'all').lower()

    if t_type not in ['all', 'department', 'course', 'year']:
        query['type'] = t_type
    
    # Department is applicable if type is student/faculty/alumni or explicitly "department"
    dept = target_dict.get('department')
    if dept:
        query['department'] = {"$regex": f"^{dept}$", "$options": "i"}
        
    # Course is applicable if type is student/alumni or explicitly "course"
    course = target_dict.get('course')
    if course:
        query['course'] = {"$regex": f"^{course}$", "$options": "i"}
        
    # Year is usually only for students or explicitly "year"
    year = target_dict.get('year')
    if year:
        query['year'] = year

    users = list(db.users.find(query))
    return users



def add_user(name, email, user_type, department, course, year, created_by):
    db = get_db()
    # Check for duplicate email
    if db.users.find_one({"email": email}):
        return None, "A user with this email already exists."

    # Strict Email Validation
    try:
        validate_email(email, check_deliverability=False)
    except EmailNotValidError as e:
        return None, str(e)

    user = {
        "user_id": str(uuid.uuid4())[:8].upper(),
        "name": name,
        "email": email,
        "type": user_type,
        "department": department,
        "course": course,
        "year": year,
        "status": "active",
        "created_by": created_by,
        "created_at": datetime.datetime.utcnow()
    }
    result = db.users.insert_one(user)
    return str(result.inserted_id), None


def update_user(user_id, name, email, user_type, department, course, year):
    db = get_db()
    try:
        db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {
                "name": name,
                "email": email,
                "type": user_type,
                "department": department,
                "course": course,
                "year": year
            }}
        )
        
        # Strict Email Validation
        try:
            validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            return False, "Invalid email format."
            
        return True, None
    except Exception as e:
        return False, str(e)


def toggle_user_status(user_id):
    db = get_db()
    try:
        user = db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            return False, "User not found."
        new_status = "inactive" if user.get("status") == "active" else "active"
        db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"status": new_status}}
        )
        return True, new_status
    except Exception as e:
        return False, str(e)


def bulk_add_users(rows, created_by):
    """
    rows: list of dicts with keys: name, email, type, department, course, year
    Returns (total_rows, success_count, duplicate_count, errors)
    """
    db = get_db()
    total = len(rows)
    success = 0
    duplicates = 0
    errors = []

    for i, row in enumerate(rows, start=1):
        email = str(row.get("email", "") or "").strip()
        if not email:
            errors.append(f"Row {i}: missing email, skipped.")
            continue
            
        if not EMAIL_REGEX.match(email):
            errors.append(f"Row {i}: invalid email format '{email}', skipped.")
            continue
            
        if db.users.find_one({"email": email}):
            duplicates += 1
            # We don't add duplicates to the errors list per user request format, 
            # they have their own count category.
            continue
            
        name = str(row.get("name", "") or "").strip()
        if not name:
            errors.append(f"Row {i}: missing name, skipped.")
            continue
            
        user_type = str(row.get("type", "student") or "student").strip().lower()
        if not user_type:
            user_type = "student"
            
        user = {
            "user_id": str(uuid.uuid4())[:8].upper(),
            "name": name,
            "email": email,
            "type": user_type,
            "department": str(row.get("department", "") or "").strip(),
            "course": str(row.get("course", "") or "").strip(),
            "year": str(row.get("year", "") or "").strip(),
            "status": "active",
            "created_by": created_by,
            "created_at": datetime.datetime.utcnow()
        }
        db.users.insert_one(user)
        success += 1

    return total, success, duplicates, errors
