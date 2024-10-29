# Task 2
from connect_mysql import connect_database
from mysql.connector import IntegrityError

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

add_workout_session(1, '2024-11-15', 30, 250)