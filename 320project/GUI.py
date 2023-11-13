import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import mysqlcreds


def query_database():
    connection = None
    try:
        # Connect to the database
        config = mysqlcreds.db_config
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(f"SELECT * FROM Employee WHERE EmployeeID = {query_entry.get()};")

        # Fetch results
        results = cursor.fetchall()
        result_text.delete(1.0, tk.END)
        print(type(results),results)
        i = 0
        columns = ["EmployeeID","FirstName","LastName","PhoneNumber","EmailAddress","Birthdate","DateOfHire","EmployeeType"]
        for row in results[0]:
            print(type(row))
            result_text.insert(tk.END, columns[i] + ": " + str(row) + '\n')
            i+=1

    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
    finally:
        if connection:
            connection.close()


# GUI setup
root = tk.Tk()
root.title("MySQL Query Tool")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Database connection details
# ttk.Label(frame, text="Host:").grid(row=0, column=0, sticky=tk.W, pady=5)
# host_entry = ttk.Entry(frame)
# host_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

# ttk.Label(frame, text="User:").grid(row=1, column=0, sticky=tk.W, pady=5)
# user_entry = ttk.Entry(frame)
# user_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

# ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky=tk.W, pady=5)
# password_entry = ttk.Entry(frame, show="*")
# password_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

# ttk.Label(frame, text="Database:").grid(row=3, column=0, sticky=tk.W, pady=5)
# database_entry = ttk.Entry(frame)
# database_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

ttk.Label(frame, text="Employee ID:").grid(row=1, column=0, sticky=tk.W, pady=5)
query_entry = ttk.Entry(frame)
query_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

execute_button = ttk.Button(frame, text="Login", command=query_database)
execute_button.grid(row=5, column=0, columnspan=2, pady=10)

result_text = tk.Text(frame, wrap=tk.WORD, width=50, height=10)
result_text.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
