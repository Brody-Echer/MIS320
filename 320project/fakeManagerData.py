##Enters data into the Manager Table
##This imports data from the employee table into the intern table with random additional data
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

# # Fetch valid ManagerIDs from the Employee table
# cursor.execute("SELECT EmployeeID FROM Manager")
# valid_manager_ids = [row[0] for row in cursor.fetchall()]

# SQL statement to select interns from the first table
select_interns_stmt = "SELECT * FROM Employee WHERE EmployeeType = 'Manager'"

# SQL statement to insert data into the second table
insert_stmt = (
    "INSERT INTO Manager (EmployeeID, Salary) "
    "VALUES (%s, %s)"
)

# Execute the select statement
cursor.execute(select_interns_stmt)

# Fetch all interns
managers = cursor.fetchall()

for manager in managers:
    employee_id = manager[0]  # Assuming EmployeeID is the first column
    salary = random.randint(70000,100000)

    
    # Data tuple
    data = (employee_id, salary)

    # Execute the insert statement for the second table
    cursor.execute(insert_stmt, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Inserted {len(managers)} manager records into the second table.")
