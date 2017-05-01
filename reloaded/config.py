import logging


class Settings():
    """configue all required settings"""

    logger = None
    config = {}

    def __init__(self):
        Settings.logger = self.configure_logger()
        Settings.config = self.config()
        pass

    def configure_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('./logs/debug.log')
        handler.setLevel(logging.INFO)
        format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(format)
        logger.addHandler(handler)
        return logger

    def config(self):
        config = {}
        config['baseUrl'] = "https://tesseract-cloud2.co.uk/"
        config['sourceString'] = "?source=wn93kn83"
        config['user'] = "kieranw"
        config['pass'] = "kieranw"
        config['max_wait_time'] = 10
        config['workshop_site'] = 'STOWS'
        return config
