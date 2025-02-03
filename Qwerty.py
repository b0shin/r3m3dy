import mysql.connector

# Define connection parameters
config = {
    'user': 'sq',
    'password': '<F33lthat>',
    'host': 'localhost',
    'database': 'infound',
}

# Establish connection
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Define your queries here
        queries = [
            "SELECT DATABASE infound ();",
            # Add more queries as needed
            "SELECT * FROM shaheens LIMIT 10;"  # Example query
        ]

        # Execute the queries
        for query in queries:
            try:
                cursor.execute(query)
                if cursor.with_rows:
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                else:
                    connection.commit()
                    print(f"Query executed successfully: {cursor.rowcount} rows affected.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
