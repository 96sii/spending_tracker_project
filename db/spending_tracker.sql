DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS categories;


CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category_id INT references categories(id)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT NOT NULL,
    date DATE NOT NULL,
    merchant_id INT references merchants(id)
);

INSERT INTO categories (category) VALUES ('Groceries');
INSERT INTO categories (category) VALUES ('Entertainment');
INSERT INTO categories (category) VALUES ('Dining out');
INSERT INTO categories (category) VALUES ('Miscellaneous');

INSERT INTO merchants (name, category_id) VALUES ('Tesco', 1);
INSERT INTO merchants (name, category_id) VALUES ('Netflix', 2);
INSERT INTO merchants (name, category_id) VALUES ('Wagamamas', 3);

INSERT INTO transactions (amount, date, merchant_id) VALUES (5.50, '2021-09-14', 1);
INSERT INTO transactions (amount, date, merchant_id) VALUES (14.99, '2021-09-14', 2);
INSERT INTO transactions (amount, date, merchant_id) VALUES (34.50, '2021-09-14', 3);


SELECT * FROM merchants;
SELECT * FROM categories;
SELECT * FROM transactions;



