# Task 3
from connect_mysql import connect_database
from mysql.connector import IntegrityError

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
        except IntegrityError:#not 100% sure this is necessary but I have it for the others
            print(f"Error: Could not update age for Member ID {member_id}.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Unable to connect to database.")

update_member_age(1, 25)