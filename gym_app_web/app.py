from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DB = 'gym_users.db'

# ---------- Initialize Database ----------
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# ---------- Routes ----------
@app.route('/')
def login():
    print("Rendering login.html")  # Add this
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def handle_login():
    username_or_email = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE (username=? OR email=?) AND password=?",
              (username_or_email, username_or_email, password))
    user = c.fetchone()
    conn.close()

    if user:
        flash(f"Welcome, {username_or_email}!", "success")
        return redirect(url_for('login'))
    else:
        flash("Invalid credentials", "danger")
        return redirect(url_for('login'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def handle_register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if not username or not email or not password:
        flash("All fields are required.", "warning")
        return redirect(url_for('register'))

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                  (username, password, email))
        conn.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for('login'))
    except sqlite3.IntegrityError:
        flash("Username already exists.", "danger")
        return redirect(url_for('register'))
    finally:
        conn.close()

# ---------- Run the App ----------
if __name__ == '__main__':
    init_db()
    app.run(debug=True, use_reloader=True)
