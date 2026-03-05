from database.mongo import get_db
from email_validator import validate_email, EmailNotValidError

def get_recipients_by_type(type_list):
    db = get_db()
    recipients = db.recipients.find({"type": {"$in": type_list}})
    return list(recipients)
    
def add_recipient(name, email, r_type, course=None):
    db = get_db()
    recipient = {
        "name": name,
        "email": email,
        "type": r_type,
        "course": course
    }
    # Strict Email Validation
    try:
        validate_email(email, check_deliverability=False)
    except EmailNotValidError as e:
        # For this specific module, we'll just raise/return or let it pass if not handled by caller
        # but it's better to validate before insertion.
        raise ValueError(f"Invalid email: {str(e)}")

    db.recipients.insert_one(recipient)
