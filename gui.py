import tkinter as tk
from tkinter import *
from tkinter import  Frame, Listbox, Scrollbar,messagebox
from main import tasks, add_task, delete_task, mark_task_complete, edit_task, sort_by_due_date,sort_by_name

root=Tk()
root.title("Timebound App")
root.geometry("700x500+400+100")
root.resizable(False,False)

def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task.get('completed', False) else " "
        listbox.insert(tk.END, f"{task['name']} (Due: {task['due_date']})")


def add_task_gui():
    task_name = task_entry.get()
    due_date = due_date_entry.get()
    if add_task(task_name, due_date):
        messagebox.showinfo("Success", "Task added successfully!")
        refresh_listbox()
    else:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")


def delete_task_gui():
    try:
        selected_index = listbox.curselection()[0]
        if delete_task(selected_index):
            messagebox.showinfo("Success", "Task deleted successfully!")
            refresh_listbox()
        else:
            messagebox.showerror("Error", "Task not found.")
    except IndexError:
        messagebox.showerror("Error", "No task selected.")

    
def mark_complete_gui():
    try:
        selected_index = listbox.curselection()[0]
        if mark_task_complete(selected_index):
            messagebox.showinfo("Success", f"Task '{tasks[selected_index]['name']}' marked as complete!")
            refresh_listbox()
        else:
            messagebox.showerror("Error", "Task not found.")
    except IndexError:
        messagebox.showerror("Error", "No task selected.")


def edit_task_gui():
    try:
        selected_index = listbox.curselection()[0]
        new_name = task_entry.get()
        new_due_date = due_date_entry.get()
        task = edit_task(selected_index, new_name, new_due_date)
        if task:
            messagebox.showinfo("Success", f"Task updated to '{task['name']}' (Due: {task['due_date']})")
            refresh_listbox()
        else:
            messagebox.showerror("Error", "Task not found.")
    except IndexError:
        messagebox.showerror("Error", "No task selected.")


def sort_by_due_date_gui():
    sort_by_due_date()
    refresh_listbox()

def sort_by_name_gui():
    sort_by_name()
    refresh_listbox()



task_frame = tk.Frame(root)
task_frame.pack(pady=10)

tk.Label(task_frame, text="Task:").grid(row=0, column=0, padx=5)
task_entry = tk.Entry(task_frame)
task_entry.grid(row=0, column=1, padx=5)

tk.Label(task_frame, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5)
due_date_entry = tk.Entry(task_frame)
due_date_entry.grid(row=1, column=1, padx=5)

tk.Button(task_frame, text="Add Task", command=add_task_gui).grid(row=2, column=0, padx=5, pady=5, sticky='ew')
tk.Button(task_frame, text="Delete Task", command=delete_task_gui ).grid(row=2, column=1, padx=5, pady=5, sticky='ew')
tk.Button(task_frame, text="Mark Complete",command=mark_complete_gui ).grid(row=2, column=2, padx=5, pady=5, sticky='ew')
tk.Button(task_frame, text="Edit Task",command=edit_task_gui ).grid(row=2, column=3, padx=5, pady=5, sticky='ew')

tk.Button(task_frame, text="Sort by Due Date", command=sort_by_due_date_gui).grid(row=3, column=0, padx=5, pady=5, sticky='ew')
tk.Button(task_frame, text="Sort by Name", command=sort_by_name_gui).grid(row=3, column=1, padx=5, pady=5, sticky='ew')


# Ensure columns expand proportionally
task_frame.grid_columnconfigure(0, weight=1)
task_frame.grid_columnconfigure(1, weight=1)
task_frame.grid_columnconfigure(2, weight=1)
task_frame.grid_columnconfigure(3, weight=1)

#frame for the listbox and scrollbar
listbox_frame = Frame(root, bd=3, width=700, height=280, bg="#32405b")
listbox_frame.pack(fill=tk.BOTH, padx=10, pady=(0, 10))

# the listbox widget
listbox = Listbox(listbox_frame, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)

#scrollbar widget
scrollbar = Scrollbar(listbox_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the listbox to use the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()