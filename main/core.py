import cmd
from main.sqlconnect import connect, create
from main.utils import startproject

class MyCLI(cmd.Cmd):
        
    prompt = '>> '
    intro = 'Welcome to Time Tracking CLI. Your Personal Time Keeper!!! Type "help" for more information'

    def do_connect_to_DB(self, line):
        """Connects to the Database"""
        connect()

    def do_create_db(self, line):
        """Creates a new database: Command is: create_db <db_name>"""
        create(line)

    def do_startproject(self, line):
        """Lets you start a project """
        startproject.start_project(line)

    def do_exit(self, line):
        """Exits the program"""
        print('Exiting the Time Tracking CLI...')
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()   