# src/data_access/db_modules/db_connections.py
import sqlite3
from utils.custom_logging import logger, error_handler
from configs.config_manager import ConfigurationManager
from configs.config_modules.messages_config import get_db_error_messages
from .db_custom_exceptions import ConnectionError

class DatabaseConnections:
    def __init__(self):
        self.connection = None
        self.config_manager = ConfigurationManager()  # Initialize ConfigurationManager

    @error_handler
    def get_connection(self):
        try:
            db_path = self.config_manager.get_path_settings()["DB_PATH"]  # Use ConfigurationManager to get DB_PATH
            connection = sqlite3.connect(db_path)
            logger.info(get_db_error_messages()["DB_CONNECTION_SUCCESS"])  # Access message through messages_config
            return connection
        except sqlite3.Error as e:
            logger.error(get_db_error_messages()["DB_CONNECTION_ERROR"].format(str(e)))  # Access message through messages_config
            raise ConnectionError(get_db_error_messages()["DB_CONNECTION_ERROR"].format(str(e))) from e

    @error_handler
    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
                logger.info(get_db_error_messages()["DB_CLOSE_SUCCESS"])  # Access message through messages_config
            except sqlite3.Error as e:
                logger.error(get_db_error_messages()["DB_CLOSE_ERROR"].format(str(e)))  # Access message through messages_config
                raise ConnectionError(get_db_error_messages()["DB_CLOSE_ERROR"].format(str(e))) from e

    @error_handler
    def close_all_connections(self):
        self.close_connection()