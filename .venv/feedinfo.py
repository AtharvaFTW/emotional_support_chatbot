import sqlite3

# Connect to the database
conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()

# Execute a query to retrieve all rows from the feedback table
cursor.execute("SELECT * FROM feedback")
rows = cursor.fetchall()

# Display the retrieved information
for row in rows:
    cleaned_comments = row[2].replace('\n', '').replace('\r', '')  # Remove newline characters
    print((row[0], row[1], cleaned_comments))  # Print the row after removing newline characters

# Close the connection
conn.close()
