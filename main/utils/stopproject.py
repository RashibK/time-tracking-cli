from main import sqlconnect
from datetime import datetime

def stop_project(name):
    
    cnx = sqlconnect.sqlconnect()
    cursor = cnx.cursor()

    try:
        get_project = """SELECT id FROM projects WHERE name=%s"""
        cursor.execute(get_project, [name])
        project_id = cursor.fetchall()

    except Exception as err:
        print(err)

    try:
        # put stop_time in the projects_time column where 
        put_stop_time = """UPDATE projects_time SET stop_time = %s WHERE stop_time IS NULL AND project_id = %s """
        cursor.execute(put_stop_time, [datetime.now(), project_id[0][0]])
        
        cnx.commit()
        print('Project Stopped successfully. Touch grass')

    except Exception as err:
        print(err)

