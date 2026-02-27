from database.mongo import get_db

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
    db.recipients.insert_one(recipient)
