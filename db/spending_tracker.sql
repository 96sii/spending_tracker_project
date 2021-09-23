DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS budgets;
DROP TABLE IF EXISTS categories;


CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    amount FLOAT NOT NULL
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT NOT NULL,
    date DATE NOT NULL,
    merchant_id INT references merchants(id),
    category_id INT references categories(id)
);

INSERT INTO categories (category) VALUES ('Bills');
INSERT INTO categories (category) VALUES ('Charity');
INSERT INTO categories (category) VALUES ('Dining out');
INSERT INTO categories (category) VALUES ('Entertainment');
INSERT INTO categories (category) VALUES ('Expenses');
INSERT INTO categories (category) VALUES ('Family');
INSERT INTO categories (category) VALUES ('Finances');
INSERT INTO categories (category) VALUES ('Gifts');
INSERT INTO categories (category) VALUES ('Groceries');
INSERT INTO categories (category) VALUES ('Holidays');
INSERT INTO categories (category) VALUES ('Miscellaneous');
INSERT INTO categories (category) VALUES ('Personal Care');
INSERT INTO categories (category) VALUES ('Shopping');
INSERT INTO categories (category) VALUES ('Transport');

INSERT INTO budgets (amount) VALUES (1400.00);












