import mysql.connector

def connect_to_database(host, user, password, database):
    """Connect to the MySQL database and return the connection."""
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

def perform_query(connection, query):
    """Execute a query and return the results."""
    cursor = connection.cursor()
    cursor.execute(query)
    
    results = cursor.fetchall()
    return results

def main():
    # Database configuration
    db_config = {
        "host": "localhost",
        "user": "brody",
        "password": "Guthix",
        "database": "3p"
    }

    # Connect to the database
    connection = connect_to_database(**db_config)

    # Perform a sample query
    query = "Describe Client;"
    results = perform_query(connection, query)
    print(results)

    # Print the results
    for row in results:
        print(row)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()
