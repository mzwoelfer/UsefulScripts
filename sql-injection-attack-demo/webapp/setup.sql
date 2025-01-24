CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    credit_card TEXT
);

INSERT INTO bookings (name, address, credit_card) VALUES ('John Smith', '123 Fake Street', '4111111111111111');
INSERT INTO bookings (name, address, credit_card) VALUES ('Jane Doe', '456 Elm Road', '5500000000000004');

