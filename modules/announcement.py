from database.mongo import get_db
import datetime

def save_announcement(title, content, targets):
    db = get_db()
    announcement = {
        "title": title,
        "content": content,
        "targets": targets,
        "created_date": datetime.datetime.utcnow()
    }
    result = db.announcements.insert_one(announcement)
    return str(result.inserted_id)

def save_log(announcement_id, name, email, r_type, status):
    db = get_db()
    log = {
        "announcement_id": announcement_id,
        "name": name,
        "email": email,
        "type": r_type,
        "status": status,
        "sent_date": datetime.datetime.utcnow()
    }
    db.announcement_logs.insert_one(log)
