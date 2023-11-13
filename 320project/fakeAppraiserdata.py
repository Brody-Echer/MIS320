##genereate fake appraiser data
import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta
import mysqlcreds

# Initialize the Faker generator
fake = Faker()

# Function to generate a random date between two dates
def random_date(start, end):
    time_between_dates = int((end - start).total_seconds())
    random_seconds = random.randint(0, time_between_dates)
    return start + timedelta(seconds=random_seconds)

# Connect to the database
config = mysqlcreds.db_config
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# SQL query to insert a new row into the Appraisers table
insert_query = """
INSERT INTO Appraiser (CompanyName, FirstName, LastName, PhoneNumber, Email, DateofHire, YearsOfExp)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

# Generate and insert 20 random rows
try:
    for _ in range(20):
        company_name = fake.company()
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()[:15]  # Ensure the phone number fits in the column
        email = fake.email()
        date_of_hire = fake.date_between(start_date='-10y', end_date='today').isoformat()
        years_of_exp = random.randint(0, 30)  # Assuming the experience is between 0 to 30 years

        cursor.execute(insert_query, (company_name, first_name, last_name, phone_number, email, date_of_hire, years_of_exp))

    # Commit the changes
    connection.commit()
    print(f"Inserted 20 random appraiser records into the database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
