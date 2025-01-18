from .. import sqlconnect

def list_all_projects():

    list_all_projects = """SELECT * FROM projects"""
    # try:
    cnx = sqlconnect.sqlconnect()
    
    try:
        cursor = cnx.cursor()
        cursor.execute(list_all_projects)
        result  = cursor.fetchall()

        if result:
            print('ID#  ProjectName              StartDate')
            print('-----------------------------------')
            for col in result:
                print(f'{col[0]}     {col[1]}            {col[2]}    ')

    except Exception as err:
        print(err)

