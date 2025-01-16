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
    id_card VARCHAR(255),                   -- Foreign key connecting to gym_members table
    sale_date DATE NOT NULL,                
    payment_method VARCHAR(255) NOT NULL,   
    sale_price DECIMAL(10, 2) NOT NULL,     -- Corrected to store prices as decimal
    expiry DATE
);
""")

# Sample member data for insertion
member_data = [
    ('IDLOVE1', '2025-01-01', 'Gcash', 1600.00, '2025-02-01'),
    ('IDLOVE2', '2025-01-01', 'Gcash', 1600.00, '2025-01-01')
]

# Execute the batch insert
cursor.executemany('''
INSERT INTO sale_table (id_card, sale_date, payment_method, sale_price, expiry)
VALUES (%s, %s, %s, %s, %s)
''', member_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

# Output confirmation
print(f"Database and table created, and records inserted: {member_data}")
