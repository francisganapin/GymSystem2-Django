import mysql.connector
from mysql.connector import Error

try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gym_db_2_django"  # Specify the database during connection
    )

    if conn.is_connected():
        print("Connected to the database successfully.")

        cursor = conn.cursor()

        # Create the table `setting_color_table`
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS setting_color_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            value VARCHAR(100),
            active BOOLEAN
        );
        """)

        print("Table `setting_color_table` created or already exists.")

        # Setting records to insert (with `name`, `color`, and `active`)
        setting_records = [
            ("Primary Color", "#462446", True),
            ("Secondary Color", "#b05f6d", True),
            ("Accent Color", "#eb6b56", True),
            ("Highlight Color", "#ffc153", True),
            ("Success Color", "#47b39d", True)
        ]

        # Execute the batch insert
        cursor.executemany('''
        INSERT INTO setting_color_table (name, value, active)
        VALUES (%s, %s, %s)
        ''', setting_records)

        # Commit the transaction
        conn.commit()

        print("Records inserted successfully into `setting_color_table`.")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
