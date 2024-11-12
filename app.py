from flask import Flask, render_template
import pymysql
from pymysql import MySQLError

app = Flask(__name__)

# Function to get the database connection
def get_db_connection():
    try:
        conn = pymysql.connect(
            host='localhost', 
            user='root',
            password='123456',
            database='my_database',
            cursorclass=pymysql.cursors.DictCursor  # Ensures that queries return dictionaries
        )
        return conn
    except MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    # Fetch data from the database
    conn = get_db_connection()
    if conn is None:
        return "Failed to connect to the database", 500
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Return the rendered template with the data
    return render_template('index.html', data=users)

if __name__ == '__main__':
    # Running the Flask app with debugging off and reloader off to avoid threading issues
    app.run(debug=False, use_reloader=False, host='127.0.0.1', port=5000)
