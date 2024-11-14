import configparser

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.config = configparser.ConfigParser()
            cls._instance.config.read('config.ini')
        return cls._instance

    def get(self, section, key):
        return self.config.get(section, key)