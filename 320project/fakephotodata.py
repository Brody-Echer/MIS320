##This inserts random data into the photographer table
import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta
import mysqlcreds

# Create a Faker instance
fake = Faker()

# Database connection parameters
config = mysqlcreds.db_config
connection = mysql.connector.connect(**config)
cursor = connection.cursor()



# Function to generate a random date
def get_random_date():
    start_date = datetime(year=1970, month=1, day=1)
    end_date = datetime.today()
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.date()

# SQL statement for inserting data
insert_stmt = (
    "INSERT INTO Photographer (CompanyName, FirstName, LastName, PhoneNumber, Email, StartDate, YearsOfExp) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)

# Number of records to insert
num_records = 10

for _ in range(num_records):
    # Generate random data
    company_name = fake.company()
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = fake.phone_number()[:15]  # Ensure the phone number fits in the column
    email = fake.email()
    start_date = get_random_date()
    years_of_exp = random.randint(0, 50)  # Assuming the experience is between 0 to 50 years

    # Data tuple
    data = (company_name, first_name, last_name, phone_number, email, start_date, years_of_exp)

    # Execute the insert statement
    cursor.execute(insert_stmt, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Inserted {num_records} records into the database.")
