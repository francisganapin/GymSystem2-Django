import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS gym_db_2_django")

cursor.execute("USE gym_db_2_django")

cursor.execute("""
CREATE TABLE gym_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_card VARCHAR(255),
    expiry DATE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(255),
    phone_number VARCHAR(255),
    address TEXT,
    profile_image VARCHAR(500)
);
""")



member_data =[
    ('IDLOVE1','2025-07-01','Test','Teresito','Male','0000000000','test address','media/images/noface.png'),
     ('IDLOVE1','2025-07-01','Test2','Teresita','Female','0000000000','test address','media/images/noface.png')
]


# Execute the batch insert
cursor.executemany('''
INSERT INTO gym_members (ID_CARD, Expiry,  First_Name, Last_Name, Gender ,Phone_Number, Address, Profile_Image)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
''', member_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Database and table created, and records inserted.")
