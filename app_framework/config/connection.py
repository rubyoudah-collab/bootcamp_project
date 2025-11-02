import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1412",
    database="skill_bootcamp"
)
cursor = db.cursor()
print("Database connection established.") 

cursor.execute("SHOW TABLES;")
for table in cursor:
    print(table)