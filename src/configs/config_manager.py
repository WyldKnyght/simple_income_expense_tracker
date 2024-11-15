# src/configs/config_manager.py
from .config_modules import db_default_data, messages_config, path_config, ui_constants

class ConfigurationManager:
    def __init__(self):
        pass

    def get_default_categories(self):
        """Get default categories from db_default_data."""
        return db_default_data.DEFAULT_CATEGORIES

    def get_default_frequencies(self):
        """Get default frequencies from db_default_data."""
        return db_default_data.DEFAULT_FREQUENCIES

    def get_db_error_messages(self):
        """Get database error messages as a dictionary."""
        return messages_config.get_db_error_messages()  # Call the function to get messages as a dictionary

    def get_ui_constants(self):
        """Get UI constants from ui_constants module."""
        return ui_constants.get_ui_constants()

    def get_path_settings(self):
        """Get path settings from path_config module."""
        return path_config.get_path_settings()

# Usage Example:
# config_manager = ConfigurationManager()
# categories = config_manager.get_default_categories()
# ui_constants = config_manager.get_ui_constants()
# paths = config_manager.get_path_settings()