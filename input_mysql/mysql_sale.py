import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS gym_db_2_django")

# Select the database
cursor.execute("USE gym_db_2_django")

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sale_table (
    id INT AUTO_INCREMENT PRIMARY KEY,      
    sale_date DATE NOT NULL,                
    payment_method VARCHAR(255) NOT NULL,   
    total_sale INT NOT NULL    -- 2/5/2025 We update this to int since we wont add decimal
);
""")

# Sample member data for insertion
member_data = [
    ('2025-01-01', 'Gcash', 1600),
    ('2025-01-01', 'Gcash', 1600)
]

# Execute the batch insert
cursor.executemany('''
INSERT INTO sale_table ( sale_date, payment_method, total_sale)
VALUES (%s, %s, %s,)
''', member_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

# Output confirmation
print(f"Database and table created, and records inserted: {member_data}")
