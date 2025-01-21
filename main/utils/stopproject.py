from main import sqlconnect
from datetime import datetime

def stop_project(name):
    
    cnx = sqlconnect.sqlconnect()
    cursor = cnx.cursor()

    try:
        get_project = """SELECT id FROM projects WHERE name=%s"""
        cursor.execute(get_project, [name])
        project_id = cursor.fetchall()

        if len(project_id) == 0:
            print(f"The project with Project Name {name} doesn't exist.")
            return
    except Exception as err:
        print(err)

    try:
        # get the start_time of this empty stop_time column
        get_start_time = """SELECT start_time FROM projects_time WHERE project_id=%s and stop_time is NULL"""
        cursor.execute(get_start_time, [project_id[0][0]])
        start_time = cursor.fetchall()

        if len(start_time) == 0:
            print('The project needs to be started before you can stop it.')
            return

        # # put stop_time in the projects_time column where 
        stop_time = datetime.now()
        put_stop_time = """UPDATE projects_time SET stop_time = %s WHERE stop_time IS NULL AND project_id = %s """
        cursor.execute(put_stop_time, [stop_time, project_id[0][0]])
        cnx.commit()

        #get current total_hours
        get_total_hours = """SELECT total_time FROM projects WHERE id = %s"""
        cursor.execute(get_total_hours, [project_id[0][0]])
        total_hours = cursor.fetchall()

        #calculate current total_hours 
        update_total_hours = """UPDATE projects SET total_time = %s WHERE id=%s"""
        cursor.execute(update_total_hours, [(int(total_hours[0][0]) ) + (stop_time - start_time[0][0]).total_seconds(), project_id[0][0]])
        cnx.commit()

        print('Project Stopped successfully. Touch grass')

    except Exception as err:
        print(err)

