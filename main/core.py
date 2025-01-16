import cmd
from sqlconnect import connect

class MyCLI(cmd.Cmd):
        
    prompt = '>> '
    intro = 'Welcome to Time Tracking CLI. Your Personal Time Keeper!!! Type "help" for more information'

    def do_connect_to_DB(self, line):
        """Connects to the Database"""
        connect()

    def do_exit(self, line):
        """Exits the program"""
        print('Exiting the Time Tracking CLI...')
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()