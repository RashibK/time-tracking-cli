from .. import sqlconnect
from datetime import datetime

def projectreport(line):
    line_list = line.split()
    try:
        if len(line_list) > 1:
            name = line_list[0]
            date = line_list[1]

            date = datetime.strptime(date, '%m/%d/%Y')

        else:
            name = line_list[0]

    except Exception as err:
        print(err)


    project_id = """SELECT id FROM projects WHERE name = %s"""
    print(name)
    cnx = sqlconnect.sqlconnect()
    
    try:
        cursor = cnx.cursor()
        cursor.execute(project_id, [name])
        projectId = cursor.fetchall()
        
        try:
            project_all_start_time = """SELECT start_time, stop_time FROM projects_time WHERE project_id = %s"""

            cursor.execute(project_all_start_time, [projectId[0][0]])
            result = cursor.fetchall()
            
            print(f'Report for Project {name}')
            print('Start Time                           Stop Time')
            print('----------------------------------------------')
            

            total_time = 0
            for row in result:
                if len(line_list) > 1:
                    if row[0].date() >= date.date():
                        print(f'{row[0]}             {row[1]}')
                        time_difference = row[1] - row[0]
                        time_difference = time_difference.total_seconds()
                        total_time += time_difference

                else:
                    print(f'{row[0]}             {row[1]}')
                    time_difference = row[1] - row[0]
                    time_difference = time_difference.total_seconds()
                    total_time += time_difference

            print('-----------------------------------------------')
            print(f'Total time spent on this project is: {int((total_time / 60) // 60)} hrs {int((total_time /60) % 60)} mins')
        except Exception as err:
            print(err)

    except Exception as err:
        print(err)


    