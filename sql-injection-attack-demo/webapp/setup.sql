CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    name TEXT
);

INSERT INTO patients (id, name) VALUES (1, 'John Smith');
INSERT INTO patients (id, name) VALUES (2, 'Jane Doe');

