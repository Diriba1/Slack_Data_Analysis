
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