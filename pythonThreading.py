import smtplib
import os

from dotenv import load_dotenv
_ = load_dotenv();

email_address = os.environ.get("EMAIL_ADDRESS")
email_password = os.environ.get("EMAIL_PASSWORD")

print(email_password)