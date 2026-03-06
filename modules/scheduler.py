from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from database.mongo import get_db
from modules.user import get_users_by_target
from utils.email_service import send_email
from modules.announcement import save_log
import atexit

def process_scheduled_announcements():
    """
    Looks for announcements in the 'Scheduled' state where
    schedule_time is <= now. Sends them and updates status to 'Sent'.
    """
    db = get_db()
    now = datetime.datetime.utcnow()
    
    # Find due announcements
    due_announcements = list(db.announcements.find({
        "status": "Scheduled",
        "schedule_time": {"$lte": now}
    }))
    
    for ann in due_announcements:
        title = ann.get("title", "Announcement")
        content = ann.get("message", "")
        # Construct target dict from flat fields
        target_dict = {
            "target_type": ann.get("target_type"),
            "department": ann.get("target_department"),
            "course": ann.get("target_course"),
            "year": ann.get("target_year")
        }
        
        recipients = get_users_by_target(target_dict)
        announcement_id = ann.get("announcement_id", str(ann.get("_id")))
        
        success_count = 0
        fail_count = 0
        
        # Dispatch emails
        for r in recipients:
            status = "Failed"
            
            # Initialize Read Tracking
            db.announcement_reads.insert_one({
                "announcement_id": announcement_id,
                "user_email": r["email"],
                "read_status": False,
                "read_time": None
            })
            
            if send_email(r["email"], title, content, announcement_id):
                status = "Sent"
                success_count += 1
            else:
                fail_count += 1
            save_log(announcement_id, r["name"], r["email"], r["type"], status)
            
        # Update announcement status to Sent
        db.announcements.update_one(
            {"_id": ann["_id"]},
            {"$set": {"status": "Sent"}}
        )
        print(f"[Scheduler] Processed announcement {announcement_id}: {success_count} sent, {fail_count} failed.")

def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=process_scheduled_announcements, trigger="interval", seconds=60)
    scheduler.start()
    
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
