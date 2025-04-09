import mysql.connector

# Function to connect to MySQL Database
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",           # Change if necessary (default is localhost)
        user="root",                # Your MySQL username
        password="Sonali1@2",        # Your MySQL password (replace with your password)
        database="sales_data_db"    # Your MySQL database name
    )
    return connection

# Function to close the MySQL database connection
def close_db_connection(connection):
    connection.close()

# Function to retrieve all sales data from the sales_data table
def get_sales_data():
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)  # Return data as a dictionary
    query = "SELECT * FROM sales_data"  # SQL query to get all data from the table
    cursor.execute(query)
    result = cursor.fetchall()  # Fetch all rows from the result of the query
    close_db_connection(connection)  # Close the connection to the database
    return result  # Return the fetched data

# Function to retrieve monthly sales data for a given platform (channel)
def get_monthly_sales(platform):
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)  # Return data as a dictionary
    query = """
    SELECT sale_date, SUM(sales) AS total_sales
    FROM sales_data
    WHERE channel = %s  # Placeholder for platform
    GROUP BY sale_date  # Grouping by sale date
    """
    cursor.execute(query, (platform,))  # Execute query with platform as the parameter
    result = cursor.fetchall()  # Fetch all rows from the result of the query
    close_db_connection(connection)  # Close the connection to the database
