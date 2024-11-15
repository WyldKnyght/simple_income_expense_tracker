# Simple Income Expense Tracker - Folder Structure

## Main Directories

### `/src` (Source Code)
- **configs/**: Configuration management
  - Default settings
  - Environment configs
  - Database schema settings
  - UI constants
- **controllers/**: Application logic
  - Main window controller
  - Database interaction handling
- **data_access/**: Database operations
  - Database management
  - Schema validation
  - Query execution
- **user_interface/**: GUI components
  - PyQt-based interfaces
  - Main window
  - Transaction views
- **utils/**: Utility functions
  - Custom logging
  - Error handling
  - Helper functions

### `/docs` (Documentation)
- **comprehensive_summary.md**: Overall system documentation
- **custom_logging_manager.md**: Logging system details
- **database_management.md**: Database architecture
- **schema_manager.md**: Schema management guide

### Root Directory
- **README.md**: Project overview
- **LICENSE**: Project licensing information

## Purpose and Usage

This structure supports:
- Clear separation of concerns
- Modular development
- Easy maintenance
- Scalable architecture
- Comprehensive documentation
- Organized configuration management

The organization makes it straightforward to:
1. Implement new features
2. Modify existing functionality
3. Debug issues
4. Maintain documentation
5. Manage configurations

## General Folder Structure
Project Root
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── data
│   ├── backups
│   └── income_expense.db
├── docs
│   ├── comprehensive_summary.md
│   ├── configuration_management.md
│   ├── custom_logging_manager.md
│   ├── database_management.md
│   ├── folder_structure.md
│   └── schema_manager.md
├── src
│   ├── configs
│   │   ├── __init__.py
│   │   ├── config_manager.py
│   │   └── config_modules
│   │       ├── __init__.py
│   │       ├── db_default_data.py
│   │       ├── db_schema.sql
│   │       ├── messages_config.py
│   │       ├── path_config.py
│   │       └── ui_constants.py
│   ├── controllers
│   │   └── main_window_controller.py
│   ├── data_access
│   │   ├── database_manager.py
│   │   ├── db_modules
│   │   │   ├── db_connections.py
│   │   │   ├── db_custom_exceptions.py
│   │   │   ├── db_initializer.py
│   │   │   ├── db_populate_default_data.py
│   │   │   ├── db_query_executor.py
│   │   │   ├── db_reset_database.py
│   │   │   └── db_validation_operations.py
│   │   ├── schema_manager.py
│   │   ├── schema_modules
│   │   │   └── schema_operations.py
│   │   └── transaction.py
│   ├── main.py
│   ├── user_interface
│   │   ├── main_window.py
│   │   ├── menu_bar.py
│   │   └── transaction_table.py
│   └── utils
│       └── custom_logging
│           ├── __init__.py
│           ├── constants.py
│           ├── decorators.py
│           ├── handlers.py
│           ├── overview.md
│           ├── setup_file_logging.py
│           └── setup_logging.py
└── tests