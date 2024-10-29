# Task 1
from connect_mysql import connect_database
from mysql.connector import IntegrityError


def add_member(id, name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_member = (id, name, age)

            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s);"

            cursor.execute(query, new_member)
            conn.commit()
            print(f"New member, {name}, has been added with ID {id}.")
        except IntegrityError:
            print(f"Error: Member ID {id} already exists")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database.")

add_member(2, "John Doe", 29)