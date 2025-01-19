from .. import sqlconnect
from datetime import datetime

def complete(name):
    cnx = sqlconnect.sqlconnect()

    change_to_completed = """UPDATE projects SET completed = 'YES', end_date = %s WHERE name = %s"""
    try:
        cursor = cnx.cursor()
        cursor.execute(change_to_completed, [datetime.now(), name])
        cnx.commit()

    except Exception as err:
        print(err)
