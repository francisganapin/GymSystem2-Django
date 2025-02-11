import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()


cursor.execute("USE gym_db_2_django")

cursor.execute("""
CREATE TABLE gym_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_card VARCHAR(255) UNIQUE,
    expiry DATE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(255),
    phone_number VARCHAR(15),
    join_date DATE,
    address VARCHAR(255),
    renewed BOOLEAN,
    profile_image VARCHAR(255)
);
""")



member_data =[
    ('IDLOVE2','2025-01-14','Test','Teresito','Male','0000000000','2021-01-01','test address','1','media/images/noface.png'),
]


# Execute the batch insert
cursor.executemany('''
INSERT INTO gym_members (ID_CARD, Expiry,  First_Name, Last_Name, Gender ,Phone_Number,Join_Date, Address,Renewed,Profile_Image)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
''', member_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Database and table created, and records inserted.")
