-- SQL-команды для создания
CREATE TABLE employees
(
employee_id SERIAL PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
title VARCHAR(100),
birth_date DATE,
notes TEXT
);

CREATE TABLE customers
(
customer_id VARCHAR(10) PRIMARY KEY,
company_name VARCHAR(50),
contact_name VARCHAR(50)
);

CREATE TABLE orders
(
order_id SERIAL PRIMARY KEY,
customer_id VARCHAR(10) REFERENCES customers(customer_id),
employee_id INTEGER REFERENCES employees(employee_id),
order_date DATE NOT NULL,
ship_city VARCHAR(50) NOT NULL
);

