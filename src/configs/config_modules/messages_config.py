# src/configs/config_modules/messages_config.py

# Database state error messages
DB_ALREADY_EXISTS_ERROR = "Database already exists"
DB_DOES_NOT_EXIST_ERROR = "Database does not exist"

# Database error messages
DB_CLOSE_ERROR = "Error closing database connection: {}"
DB_CONNECTION_ERROR = "Failed to connect to the database: {}"
DB_INIT_ERROR = "Failed to initialize the database: {}"
DB_LOAD_ERROR = "Error loading database: {}"
DB_QUERY_ERROR = "Error executing database query: {}"
DB_RESET_ERROR = "Error resetting the database: {}"
DB_SCHEMA_ERROR = "Database schema validation failed: {}"

# Success messages
DB_CLOSE_SUCCESS = "Successfully closed database connection"
DB_CONNECTION_SUCCESS = "Successfully connected to the database and loaded data"
DB_INIT_SUCCESS = "Database initialized successfully"
DB_REMOVED_SUCCESS = "Existing database removed."
DB_RESET_SUCCESS = "Database reset successfully."
DB_VALID_SUCCESS = "Database is valid."
DB_BACKUP_SUCCESS = "Database backup created successfully at: {}"

# File operation error messages
FILE_NOT_FOUND_ERROR = "File not found: {}"
FILE_READ_ERROR = "Error reading file: {}"
FILE_WRITE_ERROR = "Error writing to file: {}"

# Schema-related error messages
SCHEMA_FILE_READ_ERROR = "Failed to read schema file: {}"
SCHEMA_VALIDATION_ERROR = "Schema validation failed: {}"

# User interface error messages
UI_INITIALIZATION_ERROR = "Error initializing user interface: {}"

# Application-specific error messages
ACCOUNT_NOT_FOUND_ERROR = "Account not found with ID: {}"
CATEGORY_NOT_FOUND_ERROR = "Category not found with ID: {}"
TRANSACTION_NOT_FOUND_ERROR = "Transaction not found with ID: {}"
EXPENSE_NOT_FOUND_ERROR = "Expense not found with ID: {}"

# Data validation error messages
INVALID_INPUT_ERROR = "Invalid input: {}"
MISSING_REQUIRED_FIELD_ERROR = "Missing required field: {}"

# General error messages
UNEXPECTED_ERROR = "An unexpected error occurred: {}"

# Warning messages
DB_VALIDATION_WARNING = 'The application may not function correctly without a valid database. You can manually reset the database or make other changes as needed.'
DB_CREATE_PROMPT = 'No database found. Would you like to create a new one?'
DB_RESET_PROMPT = 'The database schema is outdated. Some features may not work. Would you like to reset the database? Warning: This will delete all existing data.'
DB_RESET_CONFIRM = "Are you sure you want to reset the database? This will delete all existing data."

def get_db_error_messages():
    """Return all relevant database error messages."""
    return {
        'DB_CONNECTION_ERROR': DB_CONNECTION_ERROR,
        'DB_INIT_ERROR': DB_INIT_ERROR,
        'DB_CLOSE_ERROR': DB_CLOSE_ERROR,
        'DB_CONNECTION_SUCCESS': DB_CONNECTION_SUCCESS,
        'DB_CLOSE_SUCCESS': DB_CLOSE_SUCCESS,
        'DB_BACKUP_SUCCESS': DB_BACKUP_SUCCESS,  # Added backup success message
        'DB_RESET_ERROR': DB_RESET_ERROR,  # Added reset error message
        'DB_REMOVED_SUCCESS': DB_REMOVED_SUCCESS,  # Ensure this message is defined
        'DB_RESET_SUCCESS': DB_RESET_SUCCESS,  # Ensure this message is defined
    }

def get_file_error_messages():
    """Return all relevant file operation error messages."""
    return {
        'FILE_NOT_FOUND_ERROR': FILE_NOT_FOUND_ERROR,
        'FILE_READ_ERROR': FILE_READ_ERROR,
        'FILE_WRITE_ERROR': FILE_WRITE_ERROR,
    }

def get_ui_error_messages():
    """Return all relevant UI error messages."""
    return {
        'UI_INITIALIZATION_ERROR': UI_INITIALIZATION_ERROR,
    }

def get_application_specific_messages():
    """Return application-specific error messages."""
    return {
        'ACCOUNT_NOT_FOUND_ERROR': ACCOUNT_NOT_FOUND_ERROR,
        'CATEGORY_NOT_FOUND_ERROR': CATEGORY_NOT_FOUND_ERROR,
        'TRANSACTION_NOT_FOUND_ERROR': TRANSACTION_NOT_FOUND_ERROR,
        'EXPENSE_NOT_FOUND_ERROR': EXPENSE_NOT_FOUND_ERROR,
    }

def get_initialization_messages():
    """Return initialization-related messages."""
    return {
        'DB_ALREADY_EXISTS_ERROR': DB_ALREADY_EXISTS_ERROR,
        'DB_INIT_SUCCESS': DB_INIT_SUCCESS,
        'DB_INIT_ERROR': DB_INIT_ERROR,
    }