# src/data_access/database_manager.py
from .db_modules.db_connections import DatabaseConnections
from .db_modules.db_initializer import DatabaseInitializer
from .db_modules.db_reset_database import ResetDatabase
from .db_modules.db_populate_default_data import DefaultDataPopulator
from .db_modules.db_query_executor import QueryExecutor
from .db_modules.db_validation_operations import ValidationOperations
from .schema_manager import SchemaManager

class DatabaseManager:
    def __init__(self):
        self.connections = DatabaseConnections()
        self.schema_manager = SchemaManager()
        self.validation_operations = ValidationOperations(self)
        self.initializer = DatabaseInitializer(self.connections, self.validation_operations)
        self.reset_db = ResetDatabase(self.connections)
        self.default_data_populator = DefaultDataPopulator(self)
        self.executor = QueryExecutor(self.connections)

    # All methods should be simple delegations to the appropriate module
    def database_exists(self):
        return self.validation_operations.database_exists()

    def validate_schema(self):
        return self.validation_operations.validate_schema()

    def initialize_database(self):
        return self.initializer.initialize_database()

    def reset_database(self):
        return self.reset_db.reset_database()

    def get_connection(self):
        return self.connections.get_connection()
    
    def new_database(self):
        return self.initializer.new_database()

    def execute_query(self, query, params=None, return_results=True):
        return self.executor.execute_query(query, params, return_results)

    def execute_insert(self, query, params=None):
        return self.executor.execute_insert(query, params)

    def populate_default_data(self):
        return self.default_data_populator.populate_all()
    
    def refresh_schema_validator(self):
        self.validation_operations.refresh_schema_cache()
