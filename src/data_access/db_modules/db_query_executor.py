# src/data_access/db_modules/db_query_executor.py
import sqlite3
from utils.custom_logging import logger, error_handler
from configs.messages_config import DB_QUERY_ERROR
from .db_custom_exceptions import QueryExecutionError

class QueryExecutor:
    def __init__(self, connections):
        self.connections = connections

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

        except sqlite3.Error as e:
            logger.error(f"Error executing query: {e}")
            if connection:
                connection.rollback()
            raise QueryExecutionError(DB_QUERY_ERROR.format(str(e))) from e
        finally:
            if connection:
                connection.close()

    @error_handler
    def execute_insert(self, query, params=None):
        return self.execute_query(query, params, return_results=False)

