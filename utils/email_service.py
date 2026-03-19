# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import config

# def send_email(to_email, title, content, announcement_id=None, smtp_account=None):
#     try:
#         from_email = smtp_account["email"] if smtp_account else config.SMTP_EMAIL
#         password = smtp_account["password"] if smtp_account else config.SMTP_PASSWORD
#         host = smtp_account["host"] if smtp_account else 'smtp.gmail.com'
#         port = int(smtp_account["port"]) if smtp_account else 587
        
#         msg = MIMEMultipart()
#         msg['From'] = from_email
#         msg['To'] = to_email
#         msg['Subject'] = f"Announcement : {title}"

#         # Create the custom HTML format to support tracking pixels
#         body = f"""Dear User,<br><br>
# A new announcement has been published.<br><br>
# Title: {title}<br>
# Message: {content}"""

#         if smtp_account and smtp_account.get("signature"):
#             # Replace newlines with <br> to preserve formatting in HTML email
#             formatted_signature = smtp_account.get("signature").replace("\n", "<br>")
#             body += f"<br><br>---<br>{formatted_signature}"
        
#         if announcement_id:
#             # We use 127.0.0.1:5000 as the dev host base. In production this would be an env var.
#             tracking_url = f"http://127.0.0.1:5000/track/{announcement_id}/{to_email}"
#             body += f'<br><img src="{tracking_url}" width="1" height="1" style="display:none;" />'

#         msg.attach(MIMEText(body, 'html'))

#         with smtplib.SMTP(host, port) as server:
#             server.starttls()
#             server.login(from_email, password)
#             server.send_message(msg)
#         return True
#     except Exception as e:
#         print(f"Error sending email to {to_email}: {e}")
#         return False











# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import config


# DEPT_DISPLAY_MAP = {
#     "SDC":   "Software Development Cell",
#     "sdc":   "Software Development Cell",
#     "CS":    "Computer Science Department",
#     "cs":    "Computer Science Department",
#     "Lib":   "Library",
#     "lib":   "Library",
#     "Exam":  "Examination Cell",
#     "Admin": "Administration",
# }

# def expand_dept_name(name):
#     """Return the full department name for known short codes, else the name as-is."""
#     if not name:
#         return name
#     return DEPT_DISPLAY_MAP.get(str(name).strip(), name)

# def send_email(to_email, title, content, announcement_id=None, smtp_account=None):
#     try:
#         from_email = smtp_account["email"] if smtp_account else config.SMTP_EMAIL
#         password = smtp_account["password"] if smtp_account else config.SMTP_PASSWORD
#         host = smtp_account["host"] if smtp_account else 'smtp.gmail.com'
#         port = int(smtp_account["port"]) if smtp_account else 587

#         # Resolve full department name for display
#         dept_name = expand_dept_name(smtp_account.get("department", "")) if smtp_account else ""
        
#         msg = MIMEMultipart()
#         # Use department as the sender name, defaulting to 'DSVV Student Club'
#         sender_name = dept_name if dept_name else "DSVV Student Club"
#         msg['From'] = f"{sender_name} <{from_email}>"
#         msg['To'] = to_email
#         msg['Subject'] = f"{title}"
#         # msg['Subject'] = f"Announcement : {title}"

#         # Create the custom HTML format to support tracking pixels
#         body = f"""
 
#  {content}"""

#         if smtp_account and smtp_account.get("signature"):
#             # Replace newlines with <br> to preserve formatting in HTML email
#             formatted_signature = smtp_account.get("signature").replace("\n", "<br>")
#             body += f"<br><br>---<br>{formatted_signature}"
        
#         if announcement_id:
#             # We use 127.0.0.1:5000 as the dev host base. In production this would be an env var.
#             tracking_url = f"http://127.0.0.1:5000/track/{announcement_id}/{to_email}"
#             body += f'<br><img src="{tracking_url}" width="1" height="1" style="display:none;" />'

#         msg.attach(MIMEText(body, 'html'))

#         with smtplib.SMTP(host, port) as server:
#             server.starttls()
#             server.login(from_email, password)
#             server.send_message(msg)
#         return True
#     except Exception as e:
#         print(f"Error sending email to {to_email}: {e}")
#         return False







import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config


DEPT_DISPLAY_MAP = {
    "SDC":   "Software Development Cell",
    "sdc":   "Software Development Cell",
    "CS":    "Computer Science Department",
    "cs":    "Computer Science Department",
    "Lib":   "Library",
    "lib":   "Library",
    "Exam":  "Examination Cell",
    "Admin": "Administration",
}


def expand_dept_name(name):
    """Return the full department name for known short codes, else the name as-is."""
    if not name:
        return name
    return DEPT_DISPLAY_MAP.get(str(name).strip(), name)


def send_email(to_email, title, content, announcement_id=None, smtp_account=None):
    try:
        # SMTP configuration
        from_email = smtp_account["email"] if smtp_account else config.SMTP_EMAIL
        password = smtp_account["password"] if smtp_account else config.SMTP_PASSWORD
        host = smtp_account["host"] if smtp_account else 'smtp.gmail.com'
        port = int(smtp_account["port"]) if smtp_account else 587

        # Department name formatting
        dept_name = expand_dept_name(smtp_account.get("department", "")) if smtp_account else ""

        # Email setup
        msg = MIMEMultipart()
        sender_name = dept_name if dept_name else "DSVV Student Club"

        msg['From'] = f"{sender_name} <{from_email}>"
        msg['To'] = to_email
        msg['Subject'] = f"{title}"

        # =========================
        # HTML EMAIL TEMPLATE
        # =========================
        body = f"""
<!DOCTYPE html>
<html>
<body style="margin:0; padding:0; background-color:#fff7ed; font-family:'Segoe UI', sans-serif;">

    <div style="max-width:650px; margin:20px auto; background:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 6px 20px rgba(0,0,0,0.1);">

        <!-- Header -->
        <div style="background: linear-gradient(135deg, #ff512f, #dd2476); padding:30px; text-align:center; color:white;">
            <h1 style="margin:0; font-size:24px;">🌺 Dev Sanskriti Vishwavidyalaya</h1>
            <p style="margin:8px 0 0;">Haridwar, Uttarakhand</p>
        </div>

        <!-- Title -->
        <div style="background:#fff1f2; padding:15px; text-align:center;">
            <h2 style="margin:0; color:#b91c1c;">🙏 आज का सत्संकल्प</h2>
        </div>

        <!-- Main Content -->
        <div style="padding:30px; color:#374151; line-height:1.7;">
            
            {content}

        </div>

        <!-- Footer -->
        <div style="background:#fde68a; padding:12px; text-align:center; font-size:12px; color:#92400e;">
            🌼 जय माता दी | &copy; 2026 Dev Sanskriti Vishwavidyalaya
        </div>

    </div>

</body>
</html>
"""

        # Tracking Pixel
        if announcement_id:
            tracking_url = f"http://127.0.0.1:5000/track/{announcement_id}/{to_email}"
            body += f'<img src="{tracking_url}" width="1" height="1" style="display:none;" />'

        # Attach email content
        msg.attach(MIMEText(body, 'html'))

        # Send Email
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)

        return True

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")
        return False