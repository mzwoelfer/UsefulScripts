CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    credit_card TEXT,
    username TEXT UNIQUE,
    password TEXT
);

INSERT INTO customers (name, address, credit_card, username, password) VALUES 
('Alice Johnson', '789 Maple Street', '4000123412341234', 'alice', 'password123'),
('Bob Williams', '101 Pine Avenue', '4111111111111111', 'bob', 'qwerty123'),
('Charlie Brown', '202 Oak Lane', '5500000000000004', 'charlie', 'letmein'),
('Diana Prince', '303 Birch Boulevard', '340000000000009', 'diana', 'wonderwoman'),
('Ethan Hunt', '404 Cedar Road', '30000000000004', 'ethan', 'mission123');

