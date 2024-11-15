# src/data_access/db_modules/db_reset_database.py
import os
import shutil
from datetime import datetime
from utils.custom_logging import logger, error_handler
from configs.config_manager import ConfigurationManager
from ..schema_manager import SchemaManager
from .db_custom_exceptions import InitializationError, QueryExecutionError

class ResetDatabase:
    def __init__(self, connections):
        self.config_manager = ConfigurationManager()  # Initialize ConfigurationManager
        self.db_path = self.config_manager.get_path_settings()["DB_PATH"]  # Get DB_PATH through ConfigurationManager
        self.backup_folder = self.config_manager.get_path_settings()["DB_BACKUP_FOLDER"]  # Get DB_BACKUP_FOLDER through ConfigurationManager
        self.connections = connections
        self.schema_manager = SchemaManager()

    @error_handler
    def reset_database(self):
        logger.info("Resetting database...")
        conn = None
        try:
            self.connections.close_all_connections()
            
            if os.path.exists(self.db_path):
                self._backup_database()
                logger.info(f"Removing existing database file: {self.db_path}")
                os.remove(self.db_path)
                logger.info(self.config_manager.get_db_error_messages()["DB_REMOVED_SUCCESS"])  # Access message through config manager
            else:
                logger.warning(f"Database file not found at {self.db_path}")

            logger.info("Creating new database with schema.")
            conn = self.connections.get_connection()
            schema_script = self.schema_manager.load_schema()
            
            if not schema_script:
                raise InitializationError("Failed to load schema script.")

            conn.executescript(schema_script)
            conn.commit()
            
            logger.info(self.config_manager.get_db_error_messages()["DB_RESET_SUCCESS"])  # Access message through config manager
            return True, self.config_manager.get_db_error_messages()["DB_RESET_SUCCESS"]
            
        except InitializationError as ie:
            error_msg = f"Initialization error: {str(ie)}"
            logger.error(error_msg)
            return False, error_msg
        except QueryExecutionError as qee:
            error_msg = f"Query execution error: {str(qee)}"
            logger.error(error_msg)
            return False, error_msg
        except Exception as e:
            error_msg = f"Unexpected error during database reset: {str(e)}"
            logger.error(error_msg)
            
            return False, self.config_manager.get_db_error_messages()["DB_RESET_ERROR"].format(error_msg)  # Access message through config manager

    def _backup_database(self):
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"family_budget_backup_{timestamp}.db"
        backup_path = os.path.join(self.backup_folder, backup_filename)
        
        shutil.copy2(self.db_path, backup_path)
        logger.info(self.config_manager.get_db_error_messages()["DB_BACKUP_SUCCESS"].format(backup_path))  # Ensure this message is defined in messages_config.py