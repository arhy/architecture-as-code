# Database connection and operations for TraderX

import psycopg2
from psycopg2 import sql
from config import DATABASE_CONFIG

@CALMDatabaseConnection("Establish a connection to the database")
def connect_to_db():
    """Establish a connection to the database."""
    try:
        connection = psycopg2.connect(
            host=DATABASE_CONFIG['host'],
            port=DATABASE_CONFIG['port'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            database=DATABASE_CONFIG['database']
        )
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None

@CALMDatabaseOperation("Create a table in the database")
def create_table(query):
    """Create a table in the database."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Error creating table: {error}")
        finally:
            connection.close()

@CALMDatabaseOperation("Insert a record into the database")
def insert_record(query, data):
    """Insert a record into the database."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Error inserting record: {error}")
        finally:
            connection.close()

@CALMDatabaseOperation("Update a record in the database")
def update_record(query, data):
    """Update a record in the database."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Error updating record: {error}")
        finally:
            connection.close()

@CALMDatabaseOperation("Delete a record from the database")
def delete_record(query, data):
    """Delete a record from the database."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Error deleting record: {error}")
        finally:
            connection.close()

@CALMDatabaseOperation("Fetch records from the database")
def fetch_records(query):
    """Fetch records from the database."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            return records
        except Exception as error:
            print(f"Error fetching records: {error}")
            return None
        finally:
            connection.close()
