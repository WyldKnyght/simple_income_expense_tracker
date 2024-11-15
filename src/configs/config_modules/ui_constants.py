# src/configs/config_modules/ui_constants.py

# Window properties
WINDOW_TITLE = "Family Budget Tracker"
WINDOW_GEOMETRY = (100, 100, 800, 600)

# Tab names
TAB_DASHBOARD = "Dashboard"
TAB_INCOMES = "Incomes"
TAB_EXPENSES = "Expenses"
TAB_TRANSACTIONS = "Transactions"
TAB_REPORTS = "Reports"

# Menu names
MENU_FILE = "File"
MENU_DATABASE = "Database"

# Menu item names
MENU_ITEM_EXIT = "Exit"
MENU_ITEM_RESET_DB = "Reset Database"
MENU_ITEM_POPULATE_DEFAULT = "Populate Default Data"

# Status bar message
STATUS_READY = "Ready"

# Placeholder text
PLACEHOLDER_TEXT = "This is the {} tab. Content coming soon!"

def get_ui_constants():
    """Return all UI constants as a dictionary."""
    return {
        "WINDOW_TITLE": WINDOW_TITLE,
        "WINDOW_GEOMETRY": WINDOW_GEOMETRY,
        "TAB_NAMES": [
            TAB_DASHBOARD,
            TAB_INCOMES,
            TAB_EXPENSES,
            TAB_TRANSACTIONS,
            TAB_REPORTS,
        ],
        "MENU_FILE": MENU_FILE,  # Add MENU_FILE here
        "MENU_DATABASE": MENU_DATABASE,  # Add MENU_DATABASE here
        "MENU_ITEM_EXIT": MENU_ITEM_EXIT,  # Add exit action name here
        "MENU_ITEM_RESET_DB": MENU_ITEM_RESET_DB,  # Add reset database action name here
        "MENU_ITEM_POPULATE_DEFAULT": MENU_ITEM_POPULATE_DEFAULT,  # Add populate default data action name here
        "STATUS_READY": STATUS_READY,
        "PLACEHOLDER_TEXT": PLACEHOLDER_TEXT,
    }