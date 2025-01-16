import os
import mysql.connector
from decouple import config
from mysql.connector import errorcode

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
    create_table = """CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255) NOT NULL, start_date DATE DEFAULT NULL, end_date DATE DEFAULT NULL)"""

    try:
        cursor.execute(create_table)

    except mysql.connector.Error as e:
        print(e.msg)

    cnx.commit()

