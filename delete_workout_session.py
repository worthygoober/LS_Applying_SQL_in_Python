# Task 4
from connect_mysql import connect_database
from mysql.connector import IntegrityError

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

delete_workout_session(1)