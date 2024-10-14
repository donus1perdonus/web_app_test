CREATE USER test_user1 WITH PASSWORD 'test';
CREATE DATABASE test_db;
GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user1;

\c test_db;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO users (name, email)
VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Alice Johnson', 'alice.johnson@example.com');
