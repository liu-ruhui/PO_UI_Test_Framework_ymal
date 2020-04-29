import os
import logging

current = os.path.dirname(__file__)
log_path = os.path.join(current,'..//logs/test.log')

class LogUtils:
    def __init__(self,logfile_path=log_path):
        self.logfile_path = logfile_path
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(level=logging.INFO)
        file_log = logging.FileHandler(self.logfile_path,encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

logger = LogUtils()
if __name__ == "__main__":
    log_utiles = LogUtils()
    log_utiles.info('newdream')