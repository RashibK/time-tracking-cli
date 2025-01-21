from .. import sqlconnect
from datetime import datetime

def complete(name):
    cnx = sqlconnect.sqlconnect()

    change_to_completed = """UPDATE projects SET completed = 'YES', end_date = %s WHERE name = %s AND completed = 'NO' """
    try:
        cursor = cnx.cursor()
        cursor.execute(change_to_completed, [datetime.now(), name])
        cnx.commit()
        print('The project is marked complete.')
    except Exception as err:
        print(err)
