from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management
app.config['DATABASE'] = 'users.db'  # Path to your SQLite database file

# Function to check user credentials against the database
def authenticate_user(username, password):
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        hashed_password = user_data[0]
        return check_password_hash(hashed_password, password)
    return False

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check user credentials against the database
        if authenticate_user(username, password):
            # Set a session variable to indicate the user is logged in
            session['logged_in'] = True
            # Redirect to the chat interface page
            return redirect(url_for('chat_interface'))
        else:
            # If credentials are incorrect, render the login page with an error message
            return render_template('login.html', error='Invalid username or password')

    # Render the login page for GET requests
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    # Clear the user's session upon logout
    session.pop('logged_in', None)
    # Redirect to the login page
    return redirect(url_for('login'))

# Chat interface route
@app.route('/chat-interface')
def chat_interface():
    # Check if the user is logged in
    if 'logged_in' not in session:
        # If not logged in, redirect to the login page
        return redirect(url_for('login'))
    # Render the chat interface page
    return render_template('chat_interface.html')

if __name__ == '__main__':
    app.run(debug=True)
