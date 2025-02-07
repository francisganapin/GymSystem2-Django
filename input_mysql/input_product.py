import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()


cursor.execute("USE gym_db_2_django")

cursor.execute("""
CREATE TABLE IF NOT EXISTS product_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    stock INT NOT NULL,
    expiry DATE NOT NULL,
    description VARCHAR(255) NOT NULL
);
""")


product_data = [
    ("Whey Protein", 35,50, "2025-12-31", "High-quality whey protein."),
    ("Creatine Monohydrate", 20,30, "2026-06-15", "Supports muscle recovery."),
    ("Mass Gainer", 40,35, "2025-09-10", "Ideal for weight gain."),
    ("Pre-Workout", 45,40, "2025-11-25", "Boosts workout performance.")
]

# Execute the batch insert
cursor.executemany('''
INSERT INTO product_table (name, price,stock, expiry, description)
VALUES (%s,%s,%s,%s,%s)
''', product_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Database and table created, and records inserted.")
