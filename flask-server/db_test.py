from db_connector import get_connection

def fetch_data_from_database():
    r = ''
    try:
       
        # Get a connection from the pool
        connection = get_connection()

        # Use the connection for your database operations
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()

        # Process the result as needed
        for row in result:
            r = row
    finally:
        # Release the connection back to the pool
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

    return str(r)
# Example usage in another Python script
fetch_data_from_database()
