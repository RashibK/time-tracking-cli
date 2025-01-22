# Project Tracker | CLI Based
Welcome to Time Tracking CLI! This command-line interface (CLI) application serves as your personal time tracker, enabling you to manage your projects, track their progress, and generate detailed reports with ease.
## Usage
To get started, use the following command in your root directory.
```python3 -m main.core```

Use the commands listed below to manage your projects:
### Commands
1. ```create_a_table```
* Connects to the database and creates a table.
* Usage: ```create_a_table```

2. ```create_db```
* Creates a new database.
* Usage: ```create_db <db_name>```

3. ```createproject```
* Creates a new project.
* Usage: ```createproject <project_name>```

4. ```startproject```
* Starts tracking a project. Make sure the project is created first.
* Usage: ```startproject <project_name>```

5. ```listallprojects```
* Lists all projects saved in the database.
* Usage: ```listallprojects```

6. ```stopproject```
* Stops tracking a project for a certain period of time.
* Usage: ```stopproject <project_name>```

7. ```report```
* Generates a report for a project.
* Usage:
  *  All-time report: ```report <project_name>```
  * Detailed report from a specific date: report ```<project_name> <month/day/year>```

8. ```complete```
* Marks a project as complete.
* Usage: complete ```<project_name>```

9. ```exit```
* Exits the CLI application.
* Usage: exit

## Contributing
Feel free to fork this repository and make improvements. If you would like to contribute, submit a pull request with your changes.
