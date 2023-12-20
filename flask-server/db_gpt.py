import mysql.connector
from mysql.connector import pooling

# Database configuration
db_config = {
  'host' :'localhost',
  'user' :'python',
  'passwd' :'password',
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
