import mysql.connector
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root1412",
        database="skill_bootcamp",
        use_pure=True
    )
    print("Database connection established.")
    cursor = db.cursor()
    print("Database connection established.") 

    cursor.execute("SHOW TABLES;")
    rows = cursor.fetchall()
    if rows:
        print("Tables in the database:")
        for (t,) in rows:
            print ("- " , t)
    else :
        print("No tables found in the database.")
    cursor.close()
    db.close()
    print("Database connection closed.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
