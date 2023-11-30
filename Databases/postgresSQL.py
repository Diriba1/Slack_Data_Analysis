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
cur.execute(
    CREATE TABLE IF NOT EXISTS messages (
    message_id SERIAL PRIMARY KEY,
    workspace_id VARCHAR(255),
    channel_id VARCHAR(255),
    user_id VARCHAR(255),
    timestamp TIMESTAMP,
    content TEXT
);

CREATE TABLE IF NOT EXISTS replies (
    reply_id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages(message_id),
    user_id VARCHAR(255),
    timestamp TIMESTAMP,
    content TEXT
);

CREATE TABLE IF NOT EXISTS reactions (
    reaction_id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages(message_id),
    user_id VARCHAR(255),
    emoji VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS sentiments (
    sentiment_id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages(message_id),
    sentiment_score FLOAT
);

CREATE TABLE IF NOT EXISTS topics (
    topic_id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages(message_id),
    topic_name VARCHAR(255)
);
)

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
