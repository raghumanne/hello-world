import mysql.connector
from mysql.connector import pooling

# Database configuration
db_config = {
  'host' :'localhost',
  'user' :'python',
  'password' :'password',
  'database' : 'mrrt'
}

# Connection pooling configuration
pool_config = {
    'pool_name': 'my_pool',
    'pool_size': 5,  # Adjust the pool size as needed
}

# Create a connection pool
connection_pool = pooling.MySQLConnectionPool(**db_config, **pool_config)


def get_connection():
    return connection_pool.get_connection()


# Example usage in another Python script
try:
    # Get a connection from the pool
    connection = get_connection()

    # Use the connection for your database operations
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE EMP (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )""")
    result = cursor.fetchall()

    # Process the result as needed
    for row in result:
        print(row)

finally:
    # Release the connection back to the pool
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
