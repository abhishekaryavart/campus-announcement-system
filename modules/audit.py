from database.mongo import get_db
import datetime
import uuid

def log_audit(user_id, action, description, ip_address):
    """
    Inserts an audit log into the `audit_logs` collection.
    
    :param user_id: ID or username of the user performing the action
    :param action: Short categorizing string (e.g., 'User login', 'User creation')
    :param description: Human readable sentence describing what happened
    :param ip_address: The requester's IP
    """
    db = get_db()
    
    audit_entry = {
        "log_id": str(uuid.uuid4())[:12],
        "user_id": user_id,
        "action": action,
        "description": description,
        "timestamp": datetime.datetime.utcnow(),
        "ip_address": ip_address
    }
    
    db.audit_logs.insert_one(audit_entry)
