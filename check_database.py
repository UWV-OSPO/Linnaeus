import sqlite3

def check_database():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()

    # Query to fetch all records from feedback_log
    cursor.execute('SELECT * FROM feedback_log')
    rows = cursor.fetchall()

    # Print each record
    for row in rows:
        print(row)

    conn.close()


# Call the function to check the database content
check_database()

