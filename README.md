Creation of the Timebound app by Group 2 !!!!

Project Title: Simple To-Do List Application

Project Description:
Create a simple to-do list application that allows users to 
1. Add tasks.
2. View tasks.
3. Remove tasks.

This project will cover fundamental Python concepts like 
-data structures
-loops
-basic user input/output.

Features to Implement:
A) Add Task:
- Allow users to add tasks to the to-do list. Each task should have a name and
a due date.

B) View Task:
- Display the list of tasks with their names and due dates

C) Remove Task: 
- Users can remove tasks from the list by specifying the task name.

D) Save/Load Tasks: 
- Implement a way to save the to-do list to a file (e.g., a text file) and
load it when the program starts.

Guidelines:

- Use dictionaries or lists to store tasks with their attributes (name and due date).
  
  We decided to go with the use of lists:
  Because they are simple to implement, intuitive, and easy to use for small-scale projects like our Timebound app

- Implement a menu-driven interface where users can choose to add, view, or remove
tasks.

- Use functions to modularize your code (e.g., separate functions for adding, viewing,
and removing tasks).

- Implement error handling to ensure the program doesn't crash when the user enters
incorrect input.

- Provide a clear and user-friendly interface with instructions for the user.

def add_task(task_name, due_date):
  try:
        # Attempt to convert the date
        datetime.strptime(due_date, '%Y-%m-%d')
        date_valid = True
  except ValueError:
        # If converting fails, the date format is incorrect
        date_valid = False

  if task_name and date_valid:
        tasks.append({'name': task_name, 'due_date': due_date})
        return True
  else:
      return False