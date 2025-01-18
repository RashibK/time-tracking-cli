import os
from datetime import datetime
from .. import sqlconnect


def create_project(name):
    if not name:
        print('You need give your project a name.')
        return 
    
    else:
        #query to create a new project to keep track of.
        create_new_project = f"""INSERT INTO projects (name, create_date)
                                 VALUES (%s, %s)"""
        try:
            cnx = sqlconnect.sqlconnect()
            cursor = cnx.cursor()
            cursor.execute(create_new_project, (name, datetime.now()))
            cnx.commit()
            print(f'Project Successfully created. Now, use the "startproject <project_name>" command to start the timer for {name} project')

        except Exception as e:
            print(e)


def start_project(name):

    start_project = f"""UPDATE projects SET current_start_date = %s WHERE name = %s"""
    
    cnx = sqlconnect.sqlconnect()   
    
    try:
        cursor = cnx.cursor()
        cursor.execute(start_project, (datetime.now(), name))
        cnx.commit()
        print('Project Started! Good luck.')
    except Exception as err:
        print(err)