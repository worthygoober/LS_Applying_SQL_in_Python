import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = 'database name'
    user = 'root'
    password = 'password'
    host = 'localhost'

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        print("Connected to MySQL database successfully.")
        return conn

    except Error as e:
        print(f"Error: {e}")
        return None
    
def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = """
            SELECT id, name, age
            FROM Members
            WHERE age BETWEEN %s AND %s;
            """

            cursor.execute(query, (start_age, end_age))
            results = cursor.fetchall()
            for member in results:
                print(f"Member ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database.")

get_members_in_age_range(25, 30)
