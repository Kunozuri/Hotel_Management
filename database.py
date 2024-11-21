import mysql.connector
from mysql.connector import Error

class SQLConnector:
    def __init__(self, host: str="localhost", user: str="root", password: str="admin", database: str="hotel_reservation"):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        
        self.connection = None

    def connect(self):
        """Establish a connection to the database."""
        try:
            print("try to connect")
            self.connection = mysql.connector.connect(
                host=self._host,
                user=self._user,
                passwd=self._password,
                database=self._database
            )
            if self.connection.is_connected():
                print("Connection to the database was successful.")
        except Error as e:
            print(f"Error while connecting to the database: {e}")

    def execute_query(self, query, params=None):
        """Execute a single query (INSERT, UPDATE, DELETE)."""
        if self.connection is None or not self.connection.is_connected():
            print("Connection is not established.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def fetch_query(self, query, params=None):
        """Execute a SELECT query and return results."""
        if self.connection is None or not self.connection.is_connected():
            print("Connection is not established.")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            cursor.close()
    
    def add_guest(self, username: str, firstname: str, lastname: str, email: str, phone: str, address: str, birthday: str):
        self.connect()
        
        try:
            sql = """
                INSERT INTO guest (username, firstname, lastname, email, phone, address, birthday)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            params = (username, firstname, lastname, email, phone, address, birthday)
            self.execute_query(sql, params)
        except Exception as e:
            print("bfhdsjf;orkf")
        
        finally:    
            self.close_connection()
            print("its addeed")


    def close_connection(self):
        """Close the database connection."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")



def test_database_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='hotel_reservation'
        )
        if connection.is_connected():
            print("Connection successful!")
    except Error:
        print("hahha")


# Example usage
if __name__ == "__main__":
    test_database_connection()
    
    db = SQLConnector()

    # Connect to the database
    db.connect()

    # Insert example
    #insert_query = "INSERT INTO guest (username, firstname, lastname) VALUES (%s, %s, %s)"
    #db.execute_query(insert_query, ("john_vbbdoe", "Jodvddhn", "Dvddgvoe"))
    insert_query = "DELETE FROM guest;"
    db.execute_query(insert_query)
    
    #db.add_guest("testuser", "Test", "User", "test@example.com", "123456789", "123 Test St", "2000-01-01")
    # Fetch example
    #fetch_query = "SELECT * FROM guest"
    #results = db.fetch_query(fetch_query)
    #for row in results:
    
    #    print(row)

    # Close connection
    db.close_connection()
