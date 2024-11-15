# src/data_access/db_modules/db_query_executor.py
from utils.custom_logging import logger, error_handler
from configs.config_manager import ConfigurationManager
from .db_custom_exceptions import QueryExecutionError

class QueryExecutor:
    def __init__(self, connections):
        self.connections = connections
        self.config_manager = ConfigurationManager()  # Initialize ConfigurationManager

    @error_handler
    def execute_query(self, query, params=None, return_results=True):
        connection = None
        try:
            connection = self.connections.get_connection()
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            result = cursor.fetchall() if return_results else None
            connection.commit()

            if query.strip().upper().startswith("INSERT"):
                return cursor.lastrowid
            else:
                return result

        except Exception as e:  # Catch all exceptions to handle sqlite3.Error and others
            logger.error(f"Error executing query: {e}")
            if connection:
                connection.rollback()
            error_message = self.config_manager.get_db_error_messages()["DB_QUERY_ERROR"].format(str(e))  # Access message through config manager
            raise QueryExecutionError(error_message) from e
        finally:
            if connection:
                connection.close()

    @error_handler
    def execute_insert(self, query, params=None):
        return self.execute_query(query, params, return_results=False)