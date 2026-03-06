# C S Broadcast System

C S Broadcast System (formerly Campus Announcement System) is a Flask-based web application that allows administrators to create and send broadcasts to selected recipients such as Students, Teachers, and Alumni using email (SMTP). The system uses MongoDB for storing recipients, announcements, and email logs.

This project is designed to simplify campus communication by providing a centralized platform for sending important updates, notices, and information with a sleek, professional UI.

---

## Features

* Rich Text Editor for creating broadcasts
* Send broadcasts via Email (SMTP)
* Target specific recipients by Role, Department, Course, or Year
* Multi-Department SMTP settings for sending from distinct official emails
* Dynamic Email Signatures based on Department
* Preview broadcast before sending
* Store and log all broadcasts in MongoDB
* Modern dashboard with dynamic Chart.js visualizations
* User management and bulk upload via Excel/CSV
* Complete Audit Logging for administrative actions

---

## Technologies Used

**Backend:**
* Python
* Flask

**Database:**
* MongoDB

**Frontend:**
* HTML5
* Bootstrap 5
* CKEditor 5
* Chart.js

**Email:**
* SMTP (Gmail supported)

---

## Installation

### 1. Clone Project or Download
```
git clone <your-repository-url>
```

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

### 3. Install Requirements
```
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create `.env` file in root:
```
MONGO_URI=mongodb://localhost:27017/
SMTP_EMAIL=global_email@gmail.com
SMTP_PASSWORD=your_app_password
```

### 5. Run Application
```
python app.py
```

Open browser:
```
http://127.0.0.1:5000
```

---

## Version History


### Version 1.0
* Basic Announcement System and public landing page.


### Version 2.0 (Current)
* **Rebranding**: Changed application name to **C S Broadcast System**.
* **UI/UX Overhaul**: Completely redesigned the dashboard to use DSVV's official blue/white color scheme, featuring professional modern data cards with SVG icons, a clean white header, and a deep blue sidebar.
* **Multi-Department SMTP**: Added the ability to manage multiple SMTP configurations per department. Emails can now be sent from department-specific addresses (e.g., Computer Science, Library, SDC).
* **Email Signatures**: Included dynamic signature support based on the selected Department SMTP account.
* **Dynamic Content**: Email subject lines now dynamically include the broadcast title.
* **Navigation**: Updated layout to include dedicated sections for Create Broadcast, Recent Broadcasts, and Important Info.


---

## License

This project is for educational and personal use.