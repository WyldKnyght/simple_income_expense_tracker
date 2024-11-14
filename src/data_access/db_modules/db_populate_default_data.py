# src/data_access/db_modules/db_populate_default_data.py

from configs.db_default_data import DEFAULT_CATEGORIES, DEFAULT_FREQUENCIES
from utils.custom_logging import logger, error_handler

class DefaultDataPopulator:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    @error_handler
    def populate_all(self):
        try:
            self._populate_categories(DEFAULT_CATEGORIES)
            self._populate_frequencies(DEFAULT_FREQUENCIES)
            logger.info("Default data populated successfully")
            return True, "Default data populated successfully"
        except Exception as e:
            error_msg = f"Error populating default data: {str(e)}"
            logger.error(error_msg)
            return False, error_msg

    def _populate_categories(self, categories, parent_id=None):
        query = "INSERT INTO Categories (category_name, parent_id) VALUES (?, ?)"
        for category in categories:
            if isinstance(category, dict):
                category_name = category.get('name')
                subcategories = category.get('subcategories', [])
            elif isinstance(category, str):
                category_name = category
                subcategories = []
            else:
                logger.error(f"Invalid category type: {type(category)}")
                continue

            category_id = self.db_manager.execute_insert(query, (category_name, parent_id))
            if subcategories:
                self._populate_categories(subcategories, category_id)

    def _populate_frequencies(self, frequencies):
        query = "INSERT INTO Frequencies (frequency_name) VALUES (?)"
        for frequency in frequencies:
            self.db_manager.execute_insert(query, (frequency,))