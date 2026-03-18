from database.mongo import get_db
import datetime

def save_announcement(title, content, priority, target_type, target_department, target_course, target_year, created_by, status="Sent", schedule_time=None, smtp_config_id=None):
    db = get_db()
    announcement = {
        "title": title,
        "message": content,
        "priority": priority,
        "target_type": target_type,
        "target_department": target_department,
        "target_course": target_course,
        "target_year": target_year,
        "created_by": created_by,
        "created_at": datetime.datetime.utcnow(),
        "status": status,
        "schedule_time": schedule_time,
        "smtp_config_id": smtp_config_id
    }
    result = db.announcements.insert_one(announcement)
    
    # Ensure announcement_id is also saved back if we want strictly 'announcement_id' inside the document, 
    # but normally MongoDB uses _id. We'll store it explicitly to match requirements perfectly:
    announcement_id_str = str(result.inserted_id)
    db.announcements.update_one({"_id": result.inserted_id}, {"$set": {"announcement_id": announcement_id_str}})
    
    return announcement_id_str

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
