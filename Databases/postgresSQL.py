import psycopg2
from psycopg2 import sql
from datetime import datetime

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="postgresdb1",
    user="post",
    password="post",
    host="localhost",
    port="5432"
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create tables
cur.execute(sql_file.sql)

# Insert sample data 
cur.execute('''
    INSERT INTO messages (workspace_id, channel_id, user_id, timestamp, content)
    VALUES (%s, %s, %s, %s, %s)
''', ('workspace_1', 'channel_123', 'user_456', datetime.now(), 'Hello, world!'))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
