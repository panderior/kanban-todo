import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','kanban_todo.settings')

import django
django.setup()

from todo.models import Column, Todo
import time

# list of data
column_list = [("To do", "report_problem", "kanban To-do"),
                            ("In progress", "build", "kanban progress"),
                            ("Done", "check_circle", "kanban  Done"),
                            ("Gone", "delete", "kanban Gone"),]

todo_list = [("Do the dishes", "Wash the dishes after dinner"),
                     ("Study lessons", "Revise the lessons learned today"),]

def populate_columns():
    for val in column_list:
        Column.objects.get_or_create(title=val[0], icon=val[1], palette=val[2])

def populate_todos():
    col_todo = Column.objects.get(title="To do")
    for todo in todo_list:
        Todo.objects.get_or_create(title=todo[0], description=todo[1], column=col_todo)


if __name__ == '__main__':
    print("Starting Kanban Todo population script ... ")
    time.sleep(1.0)
    print("Popualting Columns")
    populate_columns()
    time.sleep(1.0)
    print("Populaing Todos")
    populate_todos()