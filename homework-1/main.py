"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os
from config import FILE_PATH_CUSTUMERS, FILE_PATH_EMPLOYEES, FILE_PATH_ORDERS

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=os.getenv('pgAdmin')
)


def insert_to_bd(query, file_path):
    with open(file_path, encoding="UTF-8") as fp:
        data = csv.reader(fp)
        next(data)
        with conn.cursor() as curs:
            curs.executemany(query, data)


query_customers = "INSERT INTO customers (customer_id,company_name,contact_name) VALUES (%s, %s, %s)"

query_employees = "INSERT INTO employees (employee_id,first_name,last_name,title,birth_date,notes)" \
                  " VALUES (%s, %s, %s, %s, %s, %s)"

query_orders = "INSERT INTO orders (order_id,customer_id,employee_id,order_date,ship_city) VALUES (%s, %s, %s, %s, %s)"
insert_to_bd(query_customers, FILE_PATH_CUSTUMERS)
insert_to_bd(query_employees, FILE_PATH_EMPLOYEES)
insert_to_bd(query_orders, FILE_PATH_ORDERS)
conn.commit()
conn.close()
