import tkinter as tk
from tkinter import messagebox
import json, os

SAVE_FILE = "my_tasks.json"

def load_tasks():
    if os.path.exists(SAVE_FILE):
        try:
            return json.load(open(SAVE_FILE))
        except:
            return []
    return []

def save_tasks(tasks):
    json.dump(tasks, open(SAVE_FILE, "w"), indent=2)


class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📝 My To-Do List")
        self.geometry("400x550")
        self.resizable(False, False)
        self.configure(bg="#ffffff")
        self.tasks = load_tasks()
        self.build()
        self.show_tasks()

    def build(self):
    
        tk.Label(self, text="📝 My To-Do List",
                 font=("Helvetica", 20, "bold"),
                 bg="#ffffff", fg="#333333").pack(pady=(24, 2))

        tk.Label(self, text="What do you need to do today?",
                 font=("Helvetica", 10),
                 bg="#ffffff", fg="#999999").pack()

       
        tk.Label(self, text="Write a new task:",
                 font=("Helvetica", 11),
                 bg="#ffffff", fg="#555555", anchor="w").pack(fill="x", padx=30, pady=(20, 4))

        input_row = tk.Frame(self, bg="#ffffff")
        input_row.pack(padx=30, fill="x")

        self.task_input = tk.Entry(input_row,
                                   font=("Helvetica", 12),
                                   bg="#f0f0f0", fg="#333333",
                                   relief="flat", bd=0)
        self.task_input.pack(side="left", fill="x", expand=True,
                             ipady=8, ipadx=8)
        self.task_input.bind("<Return>", lambda e: self.add_task())

        tk.Button(input_row, text="➕ Add",
                  font=("Helvetica", 11, "bold"),
                  bg="#4CAF50", fg="white",
                  relief="flat", padx=10, pady=7,
                  cursor="hand2", command=self.add_task).pack(side="left", padx=(8, 0))

        tk.Label(self, text="Your tasks:",
                 font=("Helvetica", 11),
                 bg="#ffffff", fg="#555555", anchor="w").pack(fill="x", padx=30, pady=(20, 6))

        self.task_frame = tk.Frame(self, bg="#ffffff")
        self.task_frame.pack(fill="both", expand=True, padx=30)

        
        self.status_label = tk.Label(self, text="",
                                     font=("Helvetica", 9),
                                     bg="#ffffff", fg="#aaaaaa")
        self.status_label.pack(pady=12)


    def show_tasks(self):
        for w in self.task_frame.winfo_children():
            w.destroy()

        if not self.tasks:
            tk.Label(self.task_frame,
                     text="No tasks yet!\nAdd something above 👆",
                     font=("Helvetica", 11),
                     bg="#ffffff", fg="#cccccc",
                     justify="center").pack(pady=40)
        else:
            for i, task in enumerate(self.tasks):
                self.draw_task_row(i, task)

        done = sum(1 for t in self.tasks if t["done"])
        total = len(self.tasks)
        if total == 0:
            self.status_label.config(text="")
        elif done == total:
            self.status_label.config(text=f"🎉 All {total} tasks done!")
        else:
            self.status_label.config(text=f"{done} of {total} tasks completed")

    def draw_task_row(self, i, task):
        row = tk.Frame(self.task_frame, bg="#f9f9f9",
                       highlightbackground="#e8e8e8",
                       highlightthickness=1)
        row.pack(fill="x", pady=3)

        done_text = "✅" if task["done"] else "⬜"
        tk.Button(row, text=done_text,
                  font=("Helvetica", 14),
                  bg="#f9f9f9", relief="flat",
                  cursor="hand2",
                  command=lambda idx=i: self.toggle_done(idx)).pack(side="left", padx=6, pady=6)

        # Task title
        color = "#aaaaaa" if task["done"] else "#333333"
        font_style = ("Helvetica", 11, "overstrike") if task["done"] else ("Helvetica", 11)
        tk.Label(row, text=task["title"],
                 font=font_style, bg="#f9f9f9",
                 fg=color, anchor="w").pack(side="left", fill="x", expand=True, padx=4)

        # Delete button
        tk.Button(row, text="🗑",
                  font=("Helvetica", 13),
                  bg="#f9f9f9", fg="#ff6b6b",
                  relief="flat", cursor="hand2",
                  command=lambda idx=i: self.delete_task(idx)).pack(side="right", padx=6)

   
    def add_task(self):
        text = self.task_input.get().strip()
        if not text:
            messagebox.showinfo("Oops!", "Please type a task first ")
            return
        self.tasks.append({"title": text, "done": False})
        save_tasks(self.tasks)
        self.task_input.delete(0, "end")
        self.show_tasks()

    def toggle_done(self, i):
        self.tasks[i]["done"] = not self.tasks[i]["done"]
        save_tasks(self.tasks)
        self.show_tasks()

    def delete_task(self, i):
        title = self.tasks[i]["title"]
        if messagebox.askyesno("Delete?", f'Remove "{title}"?'):
            self.tasks.pop(i)
            save_tasks(self.tasks)
            self.show_tasks()


if __name__ == "__main__":
    ToDoApp().mainloop()
