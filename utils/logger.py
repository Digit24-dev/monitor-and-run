# New Module: utils/logger.py

import logging

class Logger:
    def __init__(self, log_file="application.log"):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger()

    def log(self, message):
        """Log a message to the file and console."""
        self.logger.info(message)
        print(message)
