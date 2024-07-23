from datetime import datetime
tasks = []

def load_tasks(fname='tasks.txt'):
    try:
        with open(fname, 'r') as file:
            for line in file:
                task_name, due_date, *completed = line.strip().split('|')
                task = {'name': task_name, 'due_date': due_date}
                if completed:
                    task['completed'] = completed[0] == 'True'
                tasks.append(task)
    except FileNotFoundError:
        pass

def save_tasks(fname='tasks.txt'):
    with open(fname, 'w') as file:
        for task in tasks:
            completed = task.get('completed', False)
            file.write(f"{task['name']}|{task['due_date']}|{completed}\n")


 


def list_tasks():
    if not tasks:
        print("Tasks are not available")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} (Due: {task['due_date']})")


def add_task(event=None):
  task_name = input("Please enter the task name: ")
  due_date = input("Enter the due date (YYYY-MM-DD): ")

  try:
        # Attempt to convert the date
        datetime.strptime(due_date, '%Y-%m-%d')
        date_valid = True
  except ValueError:
        # If converting fails, the date format is incorrect
        date_valid = False

  if task_name and date_valid:
        tasks.append({'name': task_name, 'due_date': due_date})
        print(f"Task '{task_name}' by '{due_date}' added.")
  else:
        print("Please enter a valid task name and due date in the format YYYY-MM-DD.")


def list_tasks():
    if not tasks:
        print("Tasks are not available")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} (Due: {task['due_date']})")


def mark_task_complete():
    list_tasks()
    try:
        task_to_mark = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_to_mark < len(tasks):
            tasks[task_to_mark]['completed'] = True
            save_tasks()
            print(f"Task '{tasks[task_to_mark]['name']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def edit_task():
    list_tasks()
    try:
        task_to_edit = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_to_edit < len(tasks):
            task = tasks[task_to_edit]
            new_name = input(f"Enter new name (current: {task['name']}): ")
            new_due_date = input(f"Enter new due date (current: {task['due_date']}): ")
            
            if new_name:
                task['name'] = new_name
            if new_due_date:
                try:
                    datetime.strptime(new_due_date, '%Y-%m-%d')
                    task['due_date'] = new_due_date
                except ValueError:
                    print("Invalid date format. Keeping the old due date.")
            
            save_tasks()
            print(f"Task updated to: {task['name']} (Due: {task['due_date']})")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def sort_by_due_date():
    # Sort tasks by the due date (assuming format YYYY-MM-DD for proper sorting)
    tasks.sort(key=lambda x: x['due_date'])
    print("Tasks sorted by due date.")



def sort_by_name():
    # Sort tasks by name alphabetically
    tasks.sort(key=lambda x: x['name'])
    print("Tasks sorted by name.")


def delete_task():
   list_tasks()
   try:
        taskToDelete = int(input("Enter the task number to delete: ")) - 1
        if 0 <= taskToDelete < len(tasks):
            removed_task = tasks.pop(taskToDelete)
            print(f"Task '{removed_task['name']}' deleted.")
        else:
            print("Invalid task number.")
   except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
  ### Creating loop that'll run the app & listing out the menu options
  print("Welcome to the Timebound app :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Add task")
    print("2. List task")
    print("3. Mark task as complete")
    print("4. Edit")
    print("5. Sort by due date")
    print("6. Sort by name")
    print("7. Delete task")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      add_task()
    elif (choice == "2"):
      list_tasks()
    elif (choice == "3"):
      mark_task_complete()
    elif (choice == "4"):
      edit_task()
    elif (choice == "5"):
      sort_by_due_date()
    elif (choice == "6"):
      sort_by_name()
    elif (choice == "7"):
      delete_task()
    elif (choice == "8"):
      if input("Are you sure you want to quit? (y/n): ").lower() == 'y':
         break
    # The else for err handling so that if none are chosen user can retry
    else:
      print("Invalid input. Please try again.")

  print("See you next time!!! (-.-)")