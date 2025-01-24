CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    credit_card TEXT
);

INSERT INTO bookings (name, address, credit_card) VALUES ('Alice Johnson', '789 Maple Street', '4000123412341234');
INSERT INTO bookings (name, address, credit_card) VALUES ('Bob Williams', '101 Pine Avenue', '4111111111111111');
INSERT INTO bookings (name, address, credit_card) VALUES ('Charlie Brown', '202 Oak Lane', '5500000000000004');
INSERT INTO bookings (name, address, credit_card) VALUES ('Diana Prince', '303 Birch Boulevard', '340000000000009');
INSERT INTO bookings (name, address, credit_card) VALUES ('Ethan Hunt', '404 Cedar Road', '30000000000004');
INSERT INTO bookings (name, address, credit_card) VALUES ('Fiona Apple', '505 Walnut Way', '6011000000000004');
INSERT INTO bookings (name, address, credit_card) VALUES ('George Martin', '606 Chestnut Court', '3530111333300000');
INSERT INTO bookings (name, address, credit_card) VALUES ('Hannah Montana', '707 Willow Circle', '5555555555554444');
INSERT INTO bookings (name, address, credit_card) VALUES ('Iris West', '808 Magnolia Terrace', '4111111111111111');
INSERT INTO bookings (name, address, credit_card) VALUES ('Jack Sparrow', '909 Ash Drive', '5500000000000004');
INSERT INTO bookings (name, address, credit_card) VALUES ('Karen Smith', '111 Elm Street', '4000123412341234');
INSERT INTO bookings (name, address, credit_card) VALUES ('Leo Messi', '222 Pine Avenue', '4111111111111111');
INSERT INTO bookings (name, address, credit_card) VALUES ('Megan Fox', '333 Oak Lane', '340000000000009');
INSERT INTO bookings (name, address, credit_card) VALUES ('Nathan Drake', '444 Birch Boulevard', '6011000000000004');
INSERT INTO bookings (name, address, credit_card) VALUES ('Olivia Pope', '555 Cedar Road', '3530111333300000');
INSERT INTO bookings (name, address, credit_card) VALUES ('Paul Atreides', '666 Walnut Way', '5555555555554444');
INSERT INTO bookings (name, address, credit_card) VALUES ('Quinn Fabray', '777 Chestnut Court', '4000123412341234');
INSERT INTO bookings (name, address, credit_card) VALUES ('Rachel Green', '888 Willow Circle', '4111111111111111');
INSERT INTO bookings (name, address, credit_card) VALUES ('Steve Rogers', '999 Magnolia Terrace', '5500000000000004');
INSERT INTO bookings (name, address, credit_card) VALUES ('Tony Stark', '1010 Ash Drive', '340000000000009');

