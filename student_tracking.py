import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    phone TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def add_student():
    if not first_name.get() or not last_name.get():
        messagebox.showwarning("Error", "First and Last name are required")
        return

    cursor.execute("""
        INSERT INTO students (first_name, last_name, phone, email, course)
        VALUES (?, ?, ?, ?, ?)
    """, (
        first_name.get(),
        last_name.get(),
        phone.get(),
        email.get(),
        course.get()
    ))
    conn.commit()

    clear_fields()
    load_students()

def load_students():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        listbox.insert(
            tk.END,
            f"{row[0]} | {row[1]} {row[2]} | {row[3]} | {row[4]} | {row[5]}"
        )

def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a student to delete")
        return

    value = listbox.get(selected[0])
    student_id = value.split("|")[0].strip()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    load_students()

def clear_fields():
    first_name.set("")
    last_name.set("")
    phone.set("")
    email.set("")
    course.set("")

# ---------------- UI ----------------
root = tk.Tk()
root.title("Student Tracking")
root.geometry("700x500")

# Title
tk.Label(root, text="Student Tracking", font=("Arial", 18, "bold")).pack(pady=10)

# Form frame
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

first_name = tk.StringVar()
last_name = tk.StringVar()
phone = tk.StringVar()
email = tk.StringVar()
course = tk.StringVar()

tk.Label(form_frame, text="First Name").grid(row=0, column=0)
tk.Entry(form_frame, textvariable=first_name).grid(row=0, column=1)

tk.Label(form_frame, text="Last Name").grid(row=0, column=2)
tk.Entry(form_frame, textvariable=last_name).grid(row=0, column=3)

tk.Label(form_frame, text="Phone").grid(row=1, column=0)
tk.Entry(form_frame, textvariable=phone).grid(row=1, column=1)

tk.Label(form_frame, text="Email").grid(row=1, column=2)
tk.Entry(form_frame, textvariable=email).grid(row=1, column=3)

tk.Label(form_frame, text="Course").grid(row=2, column=0)
tk.Entry(form_frame, textvariable=course).grid(row=2, column=1)

tk.Button(form_frame, text="Submit", command=add_student).grid(row=2, column=3)

# Listbox
listbox = tk.Listbox(root, width=100)
listbox.pack(pady=20)

# Delete button
tk.Button(root, text="Delete Selected Student", command=delete_student).pack()

# Load existing data
load_students()

root.mainloop()

# Close DB on exit
conn.close()
