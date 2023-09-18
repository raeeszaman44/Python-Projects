import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        # Create and configure the task listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)
        
        # Create an entry widget to input tasks
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()
        
        # Create buttons for adding, updating, and deleting tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.add_button.pack(pady=5)
        self.update_button.pack(pady=5)
        self.delete_button.pack(pady=5)
        
        # Load saved tasks from a file
        self.load_tasks()
        
    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Clear the entry widget
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_text = self.task_entry.get()
            if task_text:
                index = selected_task_index[0]
                self.tasks[index] = task_text
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)  # Clear the entry widget
                self.save_tasks()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        else:
            messagebox.showwarning("Warning", "Select a task to update.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Select a task to delete.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.update_task_listbox()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
