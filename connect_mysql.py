import mysql.connector
from mysql.connector import Error
from mysql.connector import IntegrityError

def connect_database():
    db_name = "fitness_center_db"
    user = 'root'
    password = 'Doit4Pixie&Haribo'
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

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    if duration_minutes < 0 or calories_burned < 0:
        print("Duration of exercise and calories burned must be non-negative.")
        return

    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_workout_session = (member_id, date, duration_minutes, calories_burned)

            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s);"

            cursor.execute(query, new_workout_session)
            conn.commit()
            print(f"New workout added for Member ID {member_id} on {date}.")
        except IntegrityError:
            print(f"Error: Member ID {member_id} already has a workout scheduled for {date}.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database.")

def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            #pull the specific id from the Members table
            query = "SELECT id FROM Members WHERE id = %s;"
            cursor.execute(query, (member_id, ))#remember must be tuple
            result = cursor.fetchall()

            if not result:
                print(f"Member ID {member_id} does not exist yet.")
                return
            #update age at correct member id
            query = "UPDATE Members SET age = %s WHERE id = %s;"

            cursor.execute(query, (new_age, member_id))#order here doesn't have to match order in def()
            conn.commit()
            print(f"Age updated for Member ID {member_id}.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database.")

def delete_workout_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT session_id FROM WorkoutSessions WHERE session_id = %s;"
            cursor.execute(query, (session_id, ))
            result = cursor.fetchall()

            if not result:
                print(f"Session ID {session_id} does not exist.")
                return
            
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s;"

            cursor.execute(query, (session_id, ))
            conn.commit()
            print(f"Workout session {session_id} has been deleted.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database.")

add_member(2, "John Doe", 29)
add_workout_session(1, '2024-11-15', 30, 250)
update_member_age(1, 25)
delete_workout_session(1)