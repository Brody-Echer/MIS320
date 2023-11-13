
import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta
import mysqlcreds

# Configure your MySQL connection details
config = mysqlcreds.db_config
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# Initialize the Faker generator
fake = Faker()

# Function to generate a random date of birth
def random_birthdate(age_start, age_end):
    today = datetime.today()
    start_date = today.replace(year=today.year - age_end)
    end_date = today.replace(year=today.year - age_start)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Function to generate a random date of hire
def random_date_of_hire():
    return fake.date_between(start_date='-5y', end_date='today')

# Connect to the MySQL database

cursor = connection.cursor()

# SQL query to insert a new row into the Employee table
insert_query = """
INSERT INTO Employee (FirstName, LastName, PhoneNumber, EmailAddress, Birthdate, DateOfHire, EmployeeType)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
insert_query2 = """
INSERT INTO Employee (FirstName, LastName, PhoneNumber, EmailAddress, Birthdate, DateOfHire, EmployeeType)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
# Generate and insert 100 random rows
try:
    for _ in range(10):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = ''.join(random.choices('0123456789', k=10))
        email = fake.email()
        birthdate = random_birthdate(18, 65).isoformat()
        date_of_hire = random_date_of_hire().isoformat()
        employee_type = random.choice(['Manager', 'Intern'])

        cursor.execute(insert_query, (first_name, last_name, phone_number, email, birthdate, date_of_hire, employee_type))
        cursor.execute(insert_query2,(last_name,first_name,phone_number,email, birthdate, date_of_hire, "Realtor"))
    # Commit the changes
    
    connection.commit()
    print("Inserted 20 random employee records into the database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
