import mysql.connector
import random
from datetime import datetime, timedelta
from faker import Faker

# MySQL Connection Configuration
db_config = {
    "host": "localhost",
    "user": "root",  # Change this
    "password": "root",  # Change this
    "database": "gym_db_2_django",  # Change this
}

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Faker instance
fake = Faker()

# Gender Choices
GENDER_CHOICES = ["Male", "Female"]

# SQL Insert Query
insert_query = """
INSERT INTO gym_members 
(id_card, expiry, first_name, last_name, gender, phone_number, address, join_date, renewed, profile_image) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Batch insert records
data = []
for _ in range(20000):
    id_card = fake.unique.uuid4()[:50]
    expiry = fake.date_between(start_date="today", end_date="+2y").strftime("%Y-%m-%d")
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = random.choice(GENDER_CHOICES)
    phone_number = fake.phone_number()[:15]
    address = fake.address()
    join_date = fake.date_between(start_date="-3y", end_date="today").strftime("%Y-%m-%d")
    renewed = random.choice([0, 1])
    profile_image = "images/default.jpg"

    data.append((id_card, expiry, first_name, last_name, gender, phone_number, address, join_date, renewed, profile_image))

# Insert in batches for better performance
cursor.executemany(insert_query, data)

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("✅ Successfully inserted 20,000 members into MySQL!")
