# Campus Announcement System

Campus Announcement System is a Flask-based web application that allows administrators to create and send announcements to selected recipients such as Students, Teachers, and Alumni using email (SMTP). The system uses MongoDB for storing recipients, announcements, and email logs.

This project is designed to simplify campus communication by providing a centralized platform for sending important updates, notices, and information.

---

## Features

* Rich Text Editor for creating announcements
* Send announcements via Email (SMTP)
* Target specific recipients (Student, Teacher, Alumni)
* Add and manage recipient email addresses
* Preview announcement before sending
* Store announcements in MongoDB
* Store email sending logs
* Simple and clean interface
* No login required (basic version)

---

## Technologies Used

Backend:

* Python
* Flask

Database:

* MongoDB

Frontend:

* HTML
* Bootstrap 5
* CKEditor 5

Email:

* SMTP (Gmail supported)

---

## Project Structure

```
campus-announcement-system/

app.py
config.py
requirements.txt
.env

templates/
    base.html
    index.html
    preview.html
    add_email.html

static/
    css/
    js/
    uploads/

database/
    mongo.py

modules/
    announcement.py
    recipient.py

utils/
    mail_sender.py
```

---

## Installation

### 1. Clone Project or Download

```
git clone <your-repository-url>
```

or download and extract zip.

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Linux/Mac:

```
source venv/bin/activate
```

---

### 3. Install Requirements

```
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create .env file in root:

```
MONGO_URI=mongodb://localhost:27017/
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

---

### 5. Run Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## MongoDB Database

Database Name:

```
campus_announcement_db
```

Collections:

* recipients
* announcements
* announcement_logs

---

## How to Use

Step 1:
Open Add Email page and add recipients.

Step 2:
Open Home page.

Step 3:
Write announcement.

Step 4:
Select target recipients.

Step 5:
Preview and Send.

---

## Example Use Cases

* Exam Notice
* Placement Updates
* Workshop Information
* Holiday Announcement
* Alumni Updates

---

## Future Improvements

* Login system
* Admin dashboard
* Email scheduling
* Email open tracking
* Attachment support
* WhatsApp integration

---

## Author

Abhishek Aryavart

MCA Data Science
Python Developer | Data Analyst

---

## License

This project is for educational and personal use.

---

## Version

Version 1.0 – Basic Announcement System

---

## Support

For support or suggestions, please contact the developer.











campus-announcement-system/

│── app.py
│── config.py
│── requirements.txt
│── .env

├── templates/
│     ├── base.html
│     ├── index.html
│     ├── preview.html
│     └── add_email.html

├── static/
│     ├── css/
│     │     └── style.css
│     ├── js/
│     │     └── editor.js
│     └── uploads/

├── database/
│     └── mongo.py

├── modules/
│     ├── announcement.py
│     └── recipient.py

└── utils/
      └── mail_sender.py










      Create a complete working Flask web application for my project "Campus Announcement System".

Project folder structure is already created with:

app.py
config.py
.env

templates/
    base.html
    index.html
    preview.html
    add_email.html

database/
    mongo.py

modules/
    announcement.py
    recipient.py

utils/
    mail_sender.py

static/
    css/
    js/
    uploads/


Now generate full production-ready code with the following requirements:

-----------------------------------
CORE FEATURES
-----------------------------------

1. Home Page (/)

Show:

• Announcement Title input

• Rich Text Editor (CKEditor 5 CDN)

• Target Checkboxes:

    Student
    Teacher
    Alumni

• Buttons:

    Preview
    Send Announcement


-----------------------------------

2. Add Email Page (/add-email)

Form fields:

• Name

• Email

• Type dropdown:

    student
    teacher
    alumni

• Course field (optional)

• Save Button

Save data in MongoDB collection:

recipients


-----------------------------------

3. Preview Page (/preview)

Show:

Title

Formatted Content

Targets

Send Confirmation Button


-----------------------------------

4. Send Announcement Feature

When clicking SEND:

Fetch recipient emails from MongoDB collection:

recipients

based on selected type

Send email using SMTP

Use .env config:

SMTP_EMAIL
SMTP_PASSWORD


-----------------------------------

5. MongoDB Configuration

Database name:

campus_announcement_db


Collections:

recipients

announcements

announcement_logs


-----------------------------------

6. Save Announcement

Save in announcements collection:

title

content

targets

created_date


-----------------------------------

7. Save Email Logs

Save in announcement_logs collection:

announcement_id

name

email

type

status

sent_date


-----------------------------------

8. config.py

Load from .env:

MONGO_URI

SMTP_EMAIL

SMTP_PASSWORD


-----------------------------------

9. database/mongo.py

Create MongoDB connection function

Return db object


-----------------------------------

10. mail_sender.py

Create function:

send_email(to_email, subject, content)

Use SMTP Gmail


-----------------------------------

11. recipient.py

Create function:

get_recipients_by_type(type_list)


-----------------------------------

12. announcement.py

Create functions:

save_announcement()

save_log()


-----------------------------------

13. base.html

Create navigation menu:

Home

Add Email


-----------------------------------

14. UI Requirements

Use Bootstrap 5 CDN

Clean professional design


-----------------------------------

15. app.py

Create all routes:

/

 /add-email

 /preview

 /send-announcement


-----------------------------------

16. Requirements

Use:

Flask

pymongo

python-dotenv

smtplib


-----------------------------------

IMPORTANT:

Write complete working code for ALL files.

Do NOT skip any file.

Do NOT write explanation.

ONLY write code.


-----------------------------------

FINAL GOAL:

Fully working Campus Announcement System