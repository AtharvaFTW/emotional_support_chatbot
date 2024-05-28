import sqlite3

# Connect to the database
conn = sqlite3.connect('convo.db')
cursor = conn.cursor()

# Execute a query to fetch data from a table (assuming the table name is 'users')
cursor.execute("SELECT * FROM conversation_history")
rows = cursor.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the connection
conn.close()
