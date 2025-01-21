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

    cnx = sqlconnect.sqlconnect() 
    # GET THE ID of the projectname
    try:
        get_project = """SELECT id FROM projects WHERE name=%s AND completed = 'NO' """
        cursor = cnx.cursor()
        cursor.execute(get_project, [name])

        project_id = cursor.fetchall()

        if len(project_id) == 0:
            print("Project is either marked completed or haven't been made")
            return 
        
        # check if there is already an ongoing project started with the same name
        project_started = """SELECT start_time FROM projects_time WHERE stop_time is NULL AND project_id = %s"""
        cursor.execute(project_started, [project_id[0][0]])
        result = cursor.fetchall()

        if len(result) > 0:
            print('There is already a project started under same name. Stop that before starting one again.')
        
        else:
            # start a new project_time
            start_project = f"""INSERT INTO projects_time (start_time, project_id) VALUES(%s, %s)"""
            try:
                cursor = cnx.cursor()
                cursor.execute(start_project, (datetime.now(), project_id[0][0]))
                cnx.commit()
                print('Project Started! Good luck.')
            except Exception as err:
                print(err)

    except Exception as err:
        print(err)

        