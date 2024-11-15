# src/configs/config_modules/path_config.py
import os
from dotenv import load_dotenv

load_dotenv()

class EnvSettings:
    SETTINGS = {
        'PROJECT_ROOT': 'PROJECT_ROOT',
        'ENTRY_POINT': 'ENTRY_POINT',
        'DB_PATH': 'DB_PATH',
        'DB_BACKUP_FOLDER': 'DB_BACKUP_FOLDER',
        'SCHEMA_PATH': 'SCHEMA_PATH'
    }

    def __init__(self):
        for attr, env_var in self.SETTINGS.items():
            value = os.getenv(env_var)
            if value and '${PROJECT_ROOT}' in value:
                project_root = os.getenv('PROJECT_ROOT')
                value = value.replace('${PROJECT_ROOT}', project_root)
            setattr(self, attr, value)

env_settings = EnvSettings()

# Expose the settings at the module level
for attr in EnvSettings.SETTINGS:
    globals()[attr] = getattr(env_settings, attr)

def get_path_settings():
    """Return all path settings as a dictionary."""
    return {
        "PROJECT_ROOT": env_settings.PROJECT_ROOT,
        "ENTRY_POINT": env_settings.ENTRY_POINT,
        "DB_PATH": env_settings.DB_PATH,
        "DB_BACKUP_FOLDER": env_settings.DB_BACKUP_FOLDER,
        "SCHEMA_PATH": env_settings.SCHEMA_PATH,
    }