import os
import datetime
from .. import sqlconnect



def start_project(name):
    if not name:
        print('You need give your project a name.')
        return 
    
    else:
                    #query to create a new project to keep track of.
        create_new_project = f"""INSERT INTO projects (name, start_date)
                                 VALUES (%s, %s)"""
        try:

            cnx = sqlconnect.sqlconnect()
            cursor = cnx.cursor()
            cursor.execute(create_new_project, (name, datetime.date.today()))
            cnx.commit()


        except Exception as e:
            print(e)