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

# Fetch valid ManagerIDs from the Manager table
cursor.execute("SELECT EmployeeID FROM Manager")
valid_manager_ids = [row[0] for row in cursor.fetchall()]

# SQL statement to select interns from the first table
select_interns_stmt = "SELECT * FROM Employee WHERE EmployeeType = 'Intern'"

# SQL statement to insert data into the second table
insert_stmt = (
    "INSERT INTO Intern (EmployeeID, ManagerID, Wage, School, GradDate, Tasks) "
    "VALUES (%s, %s, %s, %s, %s, %s)"
)

# Execute the select statement
cursor.execute(select_interns_stmt)

# Fetch all interns
interns = cursor.fetchall()

for intern in interns:
    employee_id = intern[0]  # Assuming EmployeeID is the first column
    manager_id = random.choice(valid_manager_ids) if valid_manager_ids else None
    wage = round(random.uniform(15.00, 30.00), 2)  # Random wage between $15 and $30
    universities = [fake.unique.company() + ' University' for _ in range(10)]
    school = random.choice(universities)  # Choose a random university from the list

    grad_date = fake.date_between(start_date='-4y', end_date='today')
    tasks = fake.sentence(nb_words=6)  # Random task description

    # Data tuple
    data = (employee_id, manager_id, wage, school, grad_date, tasks)

    # Execute the insert statement for the second table
    cursor.execute(insert_stmt, data)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Inserted {len(interns)} intern records into the second table.")
