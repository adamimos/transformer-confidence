import logging

class Logger:
    def __init__(self, log_path):
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )

    def log(self, message):
        logging.info(message)
