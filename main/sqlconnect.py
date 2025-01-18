import os
import mysql.connector
from decouple import config
from mysql.connector import errorcode

def sqlconnect():
    try:
        cnx = mysql.connector.connect(
        user= config('DB_USER'), password= config('DB_PASSWORD'),
        host = config('DB_HOST'), database= config('DB_NAME')
    )
        
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user or password credentials')

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)


def connect():
    try:
        cnx = mysql.connector.connect(
        user= config('DB_USER'), password= config('DB_PASSWORD'),
        host = config('DB_HOST'), database= config('DB_NAME')
    )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user or password credentials')

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(err)

    cursor = cnx.cursor()

    # for creating_table if it doesn't exist yet
    create_table = """CREATE TABLE projects 
    (id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    create_date DATETIME DEFAULT NULL,
    current_start_date DATETIME DEFAULT NULL,
    total_time FLOAT DEFAULT 0,
    end_date DATETIME DEFAULT NULL,
    completed VARCHAR(5) DEFAULT 'NO'
    )"""

    try:
        cursor.execute(create_table)
        print('Table succesfully created!')

    except mysql.connector.Error as e:
        print(e.msg)

    cnx.commit()

def create(db_name):

    #sql query for creating a db
    create_db = f'CREATE DATABASE {db_name}'

    try:
        cnx = mysql.connector.connect(
        user= config('DB_USER'), password= config('DB_PASSWORD'),
        host = config('DB_HOST')
    )
        cursor = cnx.cursor()

        cursor.execute(create_db)
        print('Success!')
        cnx.commit()
                

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f'Error. Database with name "{db_name}" already exists. Either create DB with another name or connect to it using connect_to_DB command.')


