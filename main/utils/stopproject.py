from main import sqlconnect
from datetime import datetime

def stop_project(name):
    
    cnx = sqlconnect.sqlconnect()
    try:
        get_data = """SELECT current_start_date FROM projects WHERE name = %s"""

        cursor = cnx.cursor()
        cursor.execute(get_data, [name])
        project_start_date = cursor.fetchall()


        # calculating the total time spent in second in current session.
        total_time = datetime.now() - project_start_date[0][0]
        total_time_seconds = (total_time.total_seconds())

        # first get the previous total time from db
        get_previous_total_time = """SELECT total_time FROM projects WHERE name = %s"""
        cursor.execute(get_previous_total_time, [name])

        previous_total_time = cursor.fetchall()
        
        #now, update the total_time column with previous + current total_time 
        add_to_total_time = """UPDATE projects SET total_time = %s"""
        cursor.execute(add_to_total_time, [total_time_seconds + previous_total_time[0][0]])

        cnx.commit()
        print('Project Stopped successfully. Touch grass')

    except Exception as err:
        print(err)
