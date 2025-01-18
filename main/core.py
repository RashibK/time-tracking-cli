import cmd
from main.sqlconnect import connect, create
from main.utils import startproject
from main.utils import listproject
from main.utils import stopproject

class MyCLI(cmd.Cmd):
        
    prompt = '>> '
    intro = 'Welcome to Time Tracking CLI. Your Personal Time Keeper!!! Type "help" for more information'

    def do_create_a_table(self, line):
        """Connects to the Database, and creating a table in db"""
        connect()

    def do_create_db(self, line):
        """Creates a new database: Command is: create_db <db_name>"""
        create(line)

    def do_createproject(self, line):
        """Lets you create a new project """
        startproject.create_project(line)

    def do_startproject(self, line):
        """Starts a project. You need to create a project before starting it. Command is: startproject <project_name>"""
        startproject.start_project(line)

    def do_listallprojects(self, line):
        """Used to list all the projects saved in a database"""
        listproject.list_all_projects()

    def do_stopproject(self, line):
        """Used to stop a project for a certain period of time"""
        stopproject.stop_project(line)

    

    def do_exit(self, line):
        """Exits the program"""
        print('Exiting the Time Tracking CLI...')
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()   