from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from flask import g
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['DATABASE'] = 'users.db'

# Function to get the database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db

# Function to close the database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        age_confirm = request.form.get('age_confirm')  # Get the value of the checkbox

        # Check if all fields are filled
        if not (username and password and confirm_password and age_confirm):
            return "All fields are required"

        # Check if password and confirm password match
        if password != confirm_password:
            return "Passwords do not match"

        # Check if age confirmation checkbox is checked
        if not age_confirm:
            return "Please confirm that you are 13 years or above"

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Insert user details into the database
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        db.commit()
        cursor.close()

        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve user from the database
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect('/index')
        else:
            return "Invalid username or password"

    return render_template('login.html')

@app.route('/index')
def index():
    if 'username' in session:
        return redirect('http://localhost:2000')
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=1000)
