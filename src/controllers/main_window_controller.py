# src/controllers/main_window_controller.py

from data_access.database_manager import DatabaseManager
from utils.custom_logging import logger, error_handler

class MainWindowController:
    def __init__(self):
        self.db_manager = DatabaseManager()

    @error_handler
    def reset_database(self, *args):
        success, message = self.db_manager.reset_database()
        if success:
            logger.info("Database reset successfully")
            # Update UI or show message to user
        else:
            logger.error(f"Failed to reset database: {message}")
            # Show error message to user

    @error_handler
    def populate_default_data(self, *args):
        success, message = self.db_manager.populate_default_data()
        if success:
            logger.info("Default data populated successfully")
            # Update UI or show success message to user
        else:
            logger.error(f"Failed to populate default data: {message}")
            # Show error message to user
