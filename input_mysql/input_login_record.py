import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()


cursor.execute("USE gym_db_2_django")

cursor.execute("""
CREATE TABLE gym_login_record (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_card VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    login_time VARCHAR(255),
    login_date VARCHAR(255)
   
);
""")




conn.commit()

# Close the connection
conn.close()

print("Database and table created, and records inserted.")
