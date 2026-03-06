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











import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

def send_email(to_email, title, content, announcement_id=None, smtp_account=None):
    try:
        from_email = smtp_account["email"] if smtp_account else config.SMTP_EMAIL
        password = smtp_account["password"] if smtp_account else config.SMTP_PASSWORD
        host = smtp_account["host"] if smtp_account else 'smtp.gmail.com'
        port = int(smtp_account["port"]) if smtp_account else 587
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = f"Announcement : {title}"

        # Create the custom HTML format to support tracking pixels
        body = f"""
Title: {title}<br>
Message: {content}"""

        if smtp_account and smtp_account.get("signature"):
            # Replace newlines with <br> to preserve formatting in HTML email
            formatted_signature = smtp_account.get("signature").replace("\n", "<br>")
            body += f"<br><br>---<br>{formatted_signature}"
        
        if announcement_id:
            # We use 127.0.0.1:5000 as the dev host base. In production this would be an env var.
            tracking_url = f"http://127.0.0.1:5000/track/{announcement_id}/{to_email}"
            body += f'<br><img src="{tracking_url}" width="1" height="1" style="display:none;" />'

        msg.attach(MIMEText(body, 'html'))

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")
        return False
