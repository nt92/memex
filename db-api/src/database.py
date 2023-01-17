import os
import psycopg2

# global connection object
conn = None


def connect_db():
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    print("***OPENING CONNECTION***")
    return connection


def get_db():
    global conn
    if conn is None:
        conn = connect_db()
    return conn
