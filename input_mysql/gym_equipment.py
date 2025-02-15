import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()


cursor.execute("USE gym_db_2_django")







# Insert gym equipment records
equipment_data = [
    ('Treadmill', 'Used for running or walking indoors', '1', 'equipment/equipment.png'),
    ('Dumbbell', 'Weight training equipment', '1', 'equipment/equipment.png'),
    ('Bench', 'For bench press and other exercises', '1', 'equipment/equipment.png'),
    ('Stationary Bike', 'Used for cardio workouts', '1', 'equipment/equipment.png'),
    ('Leg Press', 'Focuses on leg muscles', '1', 'equipment/equipment.png'),
    ('Rowing Machine', 'Simulates rowing for full-body cardio', '1', 'equipment/equipment.png'),
    ('Barbell', 'Used for weightlifting', '1', 'equipment/equipment.png'),
    ('Smith Machine', 'Assists with barbell exercises', '1', 'equipment/equipment.png'),
    ('Yoga Mat', 'Provides support for yoga exercises', '1', 'equipment/equipment.png'),
    ('Pull-Up Bar', 'Used for upper body strength exercises', '1', 'equipment/equipment.png'),
    ('Resistance Bands', 'Flexible bands for resistance training', '1', 'equipment/equipment.png'),
    ('Kettlebell', 'Used for functional strength training', '1', 'equipment/equipment.png'),
    ('Elliptical', 'Low-impact cardio machine', '1', 'equipment/equipment.png'),
    ('Medicine Ball', 'Weighted ball for strength training', '1', 'equipment/equipment.png'),
    ('Power Rack', 'Multi-use station for barbell exercises', '1', 'equipment/equipment.png'),
    ('Dip Station', 'Used for tricep dips and bodyweight exercises', '1', 'equipment/equipment.png'),
    ('Glute Bridge Machine', 'Focuses on glute muscles', '1', 'equipment/equipment.png'),
    ('Stepper', 'Simulates stair climbing for cardio', '1', 'equipment/equipment.png'),
    ('Battle Ropes', 'Used for full-body conditioning', '1', 'equipment/equipment.png'),
    ('Ab Roller', 'For abdominal muscle strengthening', '1', 'equipment/equipment.png'),
    ('Cable Machine', 'Provides resistance with a cable pulley', '1', 'equipment/equipment.png'),
    ('Plyo Box', 'Used for plyometric exercises', '1', 'equipment/equipment.png'),
    ('Leg Curl Machine', 'Targets hamstring muscles', '1', 'equipment/equipment.png'),
    ('Lat Pulldown', 'Strengthens back muscles', '1', 'equipment/equipment.png'),
    ('Preacher Curl Bench', 'For bicep isolation exercises', '1', 'equipment/equipment.png'),
    ('Weighted Vest', 'Adds resistance to bodyweight exercises', '1', 'equipment/equipment.png'),
    ('Jump Rope', 'Used for cardio and agility training', '1', 'equipment/equipment.png'),
    ('Hyperextension Bench', 'Strengthens lower back and core', '1', 'equipment/equipment.png'),
    ('Sled Push', 'Used for full-body strength and cardio', '1', 'equipment/equipment.png'),
    ('Punching Bag', 'Used for boxing and cardio workouts', '1', 'equipment/equipment.png'),
    ('Spin Bike', 'Cardio equipment for cycling indoors', '1', 'equipment/equipment.png'),
]

# Execute the batch insert
cursor.executemany('''
INSERT INTO gym_equipment_record (name,description,stock,picture)
VALUES (%s, %s, %s, %s)
''', equipment_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Database and table created, and records inserted.")
