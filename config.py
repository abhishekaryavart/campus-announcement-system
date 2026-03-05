import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# Admin & Main User credentials (set these in .env)
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@campus.edu")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

MAIN_USER_USERNAME = os.getenv("MAIN_USER_USERNAME", "mainuser")
MAIN_USER_EMAIL = os.getenv("MAIN_USER_EMAIL", "mainuser@campus.edu")
MAIN_USER_PASSWORD = os.getenv("MAIN_USER_PASSWORD", "main123")
