##Creates fake Lender data for the database
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
    "INSERT INTO Lender (FirstName, LastName, LenderType, PhoneNumber, Email, Address, InterestRate) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)

# Number of records to insert
num_records = 10

# Lender types, assuming 'PR' for Private and 'CO' for Company as examples
lender_types = ['PR', 'CO']

for _ in range(num_records):
    # Generate random data
    first_name = fake.first_name()
    last_name = fake.last_name()
    lender_type = random.choice(lender_types)
    phone_number = fake.phone_number()[:15]  # Ensure the phone number fits in the column
    email = fake.email()
    address = fake.address().replace('\n', ', ')[:50]  # Replace newlines and limit to 50 chars
    interest_rate = round(random.uniform(1.00, 20.00), 2)  # Random interest rate between 1.00 and 20.00

    # Data tuple
    data = (first_name, last_name, lender_type, phone_number, email, address, interest_rate)

    # Execute the insert statement
    cursor.execute(insert_stmt, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Inserted {num_records} records into the database.")
