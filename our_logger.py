import logging
import sys

from ZULU.constants import PATH_TO_LOGS
from ZULU.utils.convert_time_date import ConvertTimeDate


class OurLogger:
    def __init__(self):
        self.FORMAT = logging.Formatter(
            "%(name)s — %(asctime)s — %(levelname)s — %(filename)s — %(funcName)s:%(lineno)d — %(message)s")
        self.LOG_FILE_NAME = "fileLogs"
        self.PATH_TO_LOGS_FILE = PATH_TO_LOGS + "/" + self.LOG_FILE_NAME
        self.get_log_filename()

    def get_log_filename(self):
        time_now = ConvertTimeDate().get_сurrent_datetime()
        self.PATH_TO_LOGS_FILE += str(time_now) + ".log"

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.FORMAT)
        return console_handler

    def get_file_handler(self):
        file_handler = logging.FileHandler(self.PATH_TO_LOGS_FILE)
        file_handler.setFormatter(self.FORMAT)
        return file_handler

    def get_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler())
        print(logger.handlers)
        logger.propagate = False
        return logger
