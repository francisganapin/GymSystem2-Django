import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()


cursor.execute("USE gym_db_2_django")



member_data =[
    ('IDLOVE2','2025-01-014','Test','Teresito','Male','0000000000','test address','media/images/noface.png'),
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
