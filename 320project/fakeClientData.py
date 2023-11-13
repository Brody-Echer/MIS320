##This enters data into the Client table
##This creates random House Data to insert into the database
import mysqlcreds
import mysql.connector
from faker import Faker
from datetime import datetime, timedelta, date
import random

import datetime

# Create a Faker instance
fake = Faker()

# Database connection parameters
config = mysqlcreds.db_config
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

def random_birthdate(age_start, age_end):
    today = date.today()
    start_date = today.replace(year=today.year - age_end)
    end_date = today.replace(year=today.year - age_start)
    return fake.date_between(start_date=start_date, end_date=end_date)

# SQL statement for inserting data
insert_stmt = (
    "INSERT INTO Client "
    "(HouseID, LenderID, RealtorID, FirstName, LastName, Birthday)"
    "VALUES (%s, %s, %s, %s, %s, %s);"
)

# Number of records to insert
num_records = 10
house_num = 1
lend_num = 1
realtor_num = 2

print(realtor_num)


for _ in range(num_records):
    # Generate random data
    
    first_name = fake.first_name()
    last_name = fake.last_name()
    birthdate = random_birthdate(18, 65).isoformat()
    

    # Data tuple
    data = (
        house_num, lend_num, realtor_num, first_name, last_name, birthdate
    )
    house_num +=1
    lend_num +=1
    realtor_num +=2
    print("HI")
   

    # Execute the insert statement
    cursor.execute(insert_stmt, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Inserted {num_records} records into the database.")
