##This creates random House Data to insert into the database
import mysqlcreds
import mysql.connector
from faker import Faker
import random

# Create a Faker instance
fake = Faker()

# Database connection parameters
config = mysqlcreds.db_config
connection = mysql.connector.connect(**config)
cursor = connection.cursor()


# SQL statement for inserting data
insert_stmt = (
    "INSERT INTO House "
    "(PhotographerID, AppraiserID, HouseNumber, StreetName, District, City, County, "
    "Bedcount, Bathcount, Floorcount, BuildingSqFt, YardSqFt, SpeedLimit, Price) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
)

# Number of records to insert
num_records = 100

for _ in range(num_records):
    # Generate random data
    photographer_id = random.randint(1, 10)  # PhotographerID between 1 and 10
    appraiser_id = random.randint(1, 20)     # AppraiserID between 1 and 20
    house_number = random.randint(1, 9999)
    street_name = fake.street_name()[:20]    # Limit to 20 characters
    district = fake.city_suffix()[:30]       # Limit to 30 characters
    city = "Ames"                  # Limit to 30 characters
    county = "Story"                # Limit to 30 characters
    bedcount = random.randint(1, 10)
    bathcount = random.randint(1, 10)
    floorcount = random.randint(1, 5)
    building_sqft = random.randint(500, 10000)
    yard_sqft = random.randint(0, 10000)
    speed_limit = random.choice([20, 30, 40, 50, 60, 70])  # Example speed limits
    price = round(random.uniform(50000, 500000), 2)

    # Data tuple
    data = (
        photographer_id, appraiser_id, house_number, street_name, district, city, county,
        bedcount, bathcount, floorcount, building_sqft, yard_sqft, speed_limit, price
    )
    # Execute the insert statement
    cursor.execute(insert_stmt, data)
cursor.execute("INSERT INTO House (PhotographerID, AppraiserID, HouseNumber, StreetName, District, City, County, Bedcount, Bathcount, Floorcount, BuildingSqFt, YardSqFt, SpeedLimit, Price) VALUES (2,3,14,'PorchLight','East','Ames','Polk', 1, 2, 2, 5000,2000,25,200000)")

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Inserted {num_records} records into the database.")
