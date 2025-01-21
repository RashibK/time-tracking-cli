from .. import sqlconnect

import matplotlib.pyplot as plt
import numpy as np


def list_all_projects():

    list_all_projects = """SELECT * FROM projects"""
    # try:
    cnx = sqlconnect.sqlconnect()
    
    try:
        cursor = cnx.cursor()
        cursor.execute(list_all_projects)
        result  = cursor.fetchall()
        projects = []
        total_time = []
        if result:
            print('ID#  ProjectName              StartDate')
            print('-----------------------------------')
            
            for col in result:
                print(f'{col[0]}     {col[1]}            {col[2]}    ')
            
                projects.append(col[1])
                total_time.append(col[3])
        

        plt.bar(projects, total_time)
        plt.title("All Projects")
        plt.show()
    except Exception as err:
        print(err)

