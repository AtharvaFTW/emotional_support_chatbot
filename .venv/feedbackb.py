from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS extension
import sqlite3
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to create the feedback table
def create_feedback_table():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback (
                 id INTEGER PRIMARY KEY,
                 rating INTEGER,
                 comments TEXT)''')
    conn.commit()
    conn.close()

# Create the feedback table when the app starts
create_feedback_table()

@app.route('/')
def index():
    return render_template('feedback.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    try:
        rating = request.form['rating']
        comments = request.form['comments']

        print("Received feedback:", rating, comments)  # Debug message

        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute("INSERT INTO feedback (rating, comments) VALUES (?, ?)", (rating, comments))
        conn.commit()
        conn.close()

        print("Feedback stored in the database successfully")
        return jsonify({"message": "Feedback submitted successfully"})
    except Exception as e:
        error_message = "Error storing feedback in the database: " + str(e)
        print(error_message)
        return jsonify({"error": error_message}), 500  # Return a 500 Internal Server Error response

@app.route('/', methods=['POST'])  # Change to POST method
def logout():
    # Clear session or do any necessary logout operations
    return jsonify({"message": "Logged out successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
