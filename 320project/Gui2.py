import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, ttk
import mysql.connector
import mysqlcreds

class DetailsDialog:
    def __init__(self, parent, details, columns):
        self.top = Toplevel(parent)
        self.top.title("Details")

        for i, detail in enumerate(details):
            tk.Label(self.top, text=f"{columns[i]}:").grid(row=i, column=0)
            tk.Label(self.top, text=str(detail)).grid(row=i, column=1)

        close_button = tk.Button(self.top, text="Close", command=self.top.destroy)
        close_button.grid(row=len(columns), column=1)

def query_database_by_id(id, parent, user_type):
    connection = None
    try:
        config = mysqlcreds.db_config
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        if user_type == 'employee':
            query = "SELECT * FROM Employee WHERE EmployeeID = %s;"
            columns = ["EmployeeID", "FirstName", "LastName", "PhoneNumber", "EmailAddress", "Birthdate", "DateOfHire", "EmployeeType"]
        else:
            query = "SELECT * FROM Client WHERE ClientID = %s;"
            columns = ["ClientID", "HouseID", "LenderID", "FirstName", "LastName", "Birthday"]

        cursor.execute(query, (id,))
        results = cursor.fetchall()

        if results:
            DetailsDialog(parent, results[0], columns)
        else:
            messagebox.showinfo("No results", f"No {user_type} found with that ID")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
    finally:
        if connection:
            connection.close()

def ask_for_id(user_type, parent):
    id = simpledialog.askstring("Input", f"Enter your {user_type} ID", parent=parent)
    if id:
        query_database_by_id(id, parent, user_type)
    else:
        messagebox.showinfo("No ID", "No ID entered")

def on_button_click(user_type, parent):
    ask_for_id(user_type, parent)

# Create the main window
root = tk.Tk()
root.title("Client or Employee")

label_question = tk.Label(root, text="Are you a client or an employee?")
label_question.pack()

button_client = tk.Button(root, text="Client", command=lambda: on_button_click('client', root))
button_client.pack()

button_employee = tk.Button(root, text="Employee", command=lambda: on_button_click('employee', root))
button_employee.pack()




root.mainloop()
