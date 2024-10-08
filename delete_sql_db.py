import os

# Specify the path to your SQLite database file
db_file = 'feedback.db'

# Check if the file exists before trying to delete it
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"Database {db_file} deleted successfully.")
else:
    print(f"Database {db_file} does not exist.")
