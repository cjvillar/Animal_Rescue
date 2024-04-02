import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Define the SQL statements
sql_statements = [
    "INSERT INTO animal_rescue_api_animal VALUES(1,'Bear','Teddy','Male','Black Bear',0,'2022-09-09 18:22:43.596807',5,'200 lbs','ADOPTED','Mild','Honey, Photographers','5$','Alaska','profile_images/teddy.JPG')",
    "INSERT INTO animal_rescue_api_animal VALUES(3,'Dog','Phoebe','Female','Moo',0,'2022-12-02 18:58:52.873670',2,'80','AVAILABLE','Mild','pets,boops','100$','California','profile_images/Phoebe.jpg')",
    "INSERT INTO animal_rescue_api_animal VALUES(4,'Rodent','Billy','Male','Marmot',0,'2022-12-02 23:56:38.206979',100,'50','AVAILABLE','Crazy','Shred Metal, Sweet Corn','700$','Canada','profile_images/billy.JPG')",
    "INSERT INTO animal_rescue_api_animal VALUES(5,'Dog','Rick','Male','Golden Retriever',0,'2022-12-02 23:58:54.186765',1,'60','ADOPTED','Super Chill','Rally Cars, Wearing Shades','1,000,000$','California','profile_images/rick.jpg')",
    "INSERT INTO animal_rescue_api_animal VALUES(6,'Dog','Wiley','Female','Coyote',0,'2022-12-03 00:06:28.361109',1,'30','AVAILABLE','outdoorsy','rodents, wind','800$','Point Reyes','profile_images/Wiley.jpg')"
]

# Execute each SQL statement
for sql in sql_statements:
    cursor.execute(sql)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully!")
