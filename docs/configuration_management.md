### Configuration Management Structure

The app uses a centralized `ConfigurationManager` class located in `/src/configs/config_manager.py` that coordinates access to various configuration modules:

```python
class ConfigurationManager:
    def get_default_categories(self)
    def get_default_frequencies(self)
    def get_db_error_messages(self)
    def get_ui_constants(self)
    def get_path_settings()
```

### Configuration Modules

The configuration is split into specialized modules under `/src/configs/config_modules/`:

1. **Database Defaults** (`db_default_data.py`)
   - Defines default categories for expenses/income
   - Sets up transaction frequencies (weekly, monthly, etc.)

2. **Messages** (`messages_config.py`)
   - Database error messages
   - Success messages
   - File operation errors
   - UI messages

3. **Paths** (`path_config.py`)
   - Project root directory
   - Database paths
   - Schema locations
   - Backup folders

4. **UI Constants** (`ui_constants.py`)
   - Window properties
   - Tab names
   - Menu items
   - Status messages

### Usage

To use configurations in the application:

```python
config_manager = ConfigurationManager()
categories = config_manager.get_default_categories()
ui_settings = config_manager.get_ui_constants()
paths = config_manager.get_path_settings()
```

This structure provides a clean separation of concerns and makes configuration management maintainable and centralized.