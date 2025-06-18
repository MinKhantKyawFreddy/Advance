import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize DB
def init_db():
    conn = sqlite3.connect('gym_users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# Login
def login():
    username_or_email = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('gym_users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE (username=? OR email=?) AND password=?",
              (username_or_email, username_or_email, password))
    user = c.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username_or_email}!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

# Register window
def open_register_window():
    register_window = tk.Toplevel(app)
    register_window.title("Register")
    register_window.geometry("300x320")
    register_window.configure(bg="#0f0f0f")

    tk.Label(register_window, text="Create an Account", font=("Arial", 14), fg="white", bg="#0f0f0f").pack(pady=10)

    # Entry fields
    tk.Label(register_window, text="Username", fg="white", bg="#0f0f0f").pack()
    username_entry = tk.Entry(register_window, bg="#1e1e1e", fg="white", insertbackground="white")
    username_entry.pack(pady=2)

    tk.Label(register_window, text="Email", fg="white", bg="#0f0f0f").pack()
    email_entry = tk.Entry(register_window, bg="#1e1e1e", fg="white", insertbackground="white")
    email_entry.pack(pady=2)

    tk.Label(register_window, text="Password", fg="white", bg="#0f0f0f").pack()
    password_entry = tk.Entry(register_window, show="*", bg="#1e1e1e", fg="white", insertbackground="white")
    password_entry.pack(pady=2)

    # Register function now uses those entries directly
    def register_user():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if not username or not email or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        conn = sqlite3.connect('gym_users.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                      (username, password, email))
            conn.commit()
            messagebox.showinfo("Success", "Account created!")
            register_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()

    tk.Button(register_window, text="Register", command=register_user,
              bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", padx=10, pady=5).pack(pady=15)

# Main UI
app = tk.Tk()
app.title("Gym App - Login")
app.geometry("350x300")
app.configure(bg="#0f0f0f")

tk.Label(app, text="Welcome to Gym App", font=("Arial", 16, "bold"), fg="#00acee", bg="#0f0f0f").pack(pady=15)

tk.Label(app, text="Username or Email", fg="white", bg="#0f0f0f").pack()
username_entry = tk.Entry(app, bg="#1e1e1e", fg="white", insertbackground="white")
username_entry.pack(pady=5)

tk.Label(app, text="Password", fg="white", bg="#0f0f0f").pack()
password_entry = tk.Entry(app, show="*", bg="#1e1e1e", fg="white", insertbackground="white")
password_entry.pack(pady=5)

tk.Button(app, text="Login", command=login,
          bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", padx=10, pady=5).pack(pady=10)

tk.Label(app, text="Don't have an account?", fg="gray", bg="#0f0f0f").pack()
tk.Button(app, text="Register", command=open_register_window,
          bg="#222", fg="white", activebackground="#333", relief="flat").pack()

init_db()
app.mainloop()
