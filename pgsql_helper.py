import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

class PgSQLHelper:
    def __init__(self):
        load_dotenv()
        environment = os.getenv('DB_ENVIRONMENT', 'local')
        
        if environment == 'local':
            self.host = os.getenv('LOCAL_DB_HOST')
            self.port = os.getenv('LOCAL_DB_PORT')
            self.database = os.getenv('LOCAL_DB_NAME')
            self.user = os.getenv('LOCAL_DB_USER')
            self.password = os.getenv('LOCAL_DB_PASSWORD')
        else:
            self.host = os.getenv('DB_HOST')
            self.port = os.getenv('DB_PORT')
            self.database = os.getenv('DB_NAME')
            self.user = os.getenv('DB_USER')
            self.password = os.getenv('DB_PASSWORD')
        
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
                cursor_factory=RealDictCursor  # Ensure results are returned as dictionaries
            )
            print("Connection to PostgreSQL DB successful")
        except Exception as e:
            print(f"Error while connecting to PostgreSQL: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

    def execute_query(self, query, params=None):
        if not self.connection:
            print("No connection to the database.")
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print("Query executed successfully")
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch_query(self, query, params=None):
        if not self.connection:
            print("No connection to the database.")
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error fetching query: {e}")
            return None

    def execute_many(self, query, params_list):
        if not self.connection:
            print("No connection to the database.")
            return None

        try:
            with self.connection.cursor() as cursor:
                cursor.executemany(query, params_list)
                self.connection.commit()
                print("Batch query executed successfully")
        except Exception as e:
            print(f"Error executing batch query: {e}")

# Usage example:
# if __name__ == "__main__":
#     db_helper = PgSQLHelper()
#     db_helper.connect()
#     db_helper.execute_query("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR(100));")
#     db_helper.disconnect()