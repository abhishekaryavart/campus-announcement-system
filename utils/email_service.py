import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

def send_email(to_email, title, content, announcement_id=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = config.SMTP_EMAIL
        msg['To'] = to_email
        msg['Subject'] = "University Announcement"

        # Create the custom HTML format to support tracking pixels
        body = f"""Dear User,<br><br>
A new announcement has been published.<br><br>
Title: {title}<br>
Message: {content}"""
        
        if announcement_id:
            # We use 127.0.0.1:5000 as the dev host base. In production this would be an env var.
            tracking_url = f"http://127.0.0.1:5000/track/{announcement_id}/{to_email}"
            body += f'<br><img src="{tracking_url}" width="1" height="1" style="display:none;" />'

        msg.attach(MIMEText(body, 'html'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(config.SMTP_EMAIL, config.SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")
        return False
