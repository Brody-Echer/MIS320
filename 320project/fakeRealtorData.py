##This script enters data into the realtor table with random date
import mysqlcreds
import mysql.connector
import random

# Database connection parameters
config = mysqlcreds.db_config
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# SQL statement to select Realtors from the employee table
select_realtors_stmt = "SELECT EmployeeID FROM Employee WHERE EmployeeType = 'Realtor'"

# SQL statement to select Manager IDs from the manager table
select_managers_stmt = "SELECT EmployeeID FROM Manager"

# SQL statement to insert data into the realtor table
insert_realtor_stmt = (
    "INSERT INTO Realtor (EmployeeID, ManagerID, Salary, Commission) "
    "VALUES (%s, %s, %s, %s)"
)

# Execute the select statement to get Realtors
cursor.execute(select_realtors_stmt)
realtors = cursor.fetchall()

# Execute the select statement to get Managers
cursor.execute(select_managers_stmt)
managers = cursor.fetchall()
manager_ids = [manager[0] for manager in managers]

# Check if there are managers available
if not manager_ids:
    raise Exception("No managers found in the database.")

for realtor in realtors:
    employee_id = realtor[0]
    manager_id = random.choice(manager_ids)  # Randomly assign a manager
    salary = round(random.uniform(30000, 100000), 2)  # Example salary range
    commission = round(random.uniform(0.01, 0.10), 2)  # Example commission rate

    # Data tuple
    data = (employee_id, manager_id, salary, commission)

    # Execute the insert statement for the realtor table
    cursor.execute(insert_realtor_stmt, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
num_realtors = len(realtors)
print(f"Inserted {len(realtors)} realtor records into the realtor table.")
