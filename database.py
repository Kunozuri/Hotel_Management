import mysql.connector
from mysql.connector import Error
from PyQt5.QtCore import QRunnable

class SQLConnector(QRunnable):
    def __init__(self, method: str= "run", parameters: dict={}):
        """ connection to database can only be modify here """
        self.__host= "localhost"
        self.__user= "root"
        self.__passwd= "admin"
        self.__database= "hotel_reservation"
        
        
        self.parameters = parameters # expected parameter of every method
        self.method = method # method to run
        
        self.__connection = None

    def run(self):
        print("you are caliing the default run.\ndid you perhaps forgot to especify the method to run?")
    
    def __connect_db(self) -> None:
        """Establish a connection to the database."""
        try:
            print("try to connect")
            self.__connection = mysql.connector.connect(
                host= self.__host,
                user= self.__user,
                passwd= self.__passwd,
                database= self.__database
            )
            if self.__connection.is_connected():
                print("Connection to the database was successful.")
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            
    def __disconnect_db(self) -> None:
        """Close the database connection."""
        if self.__connection is not None and self.__connection.is_connected():
            self.__connection.close()
            print("Database connection closed.")
    
    def execute_query(self, sql: str, value) -> None:
        """Execute a single query (INSERT, UPDATE, DELETE)."""
        
        if self.__connection is None or not self.__connection.is_connected():
            print("Connection is not established.")
            return

        cursor = self.__connection.cursor()
        try:
            cursor.execute(sql, value)
            self.__connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")
            self.__connection.rollback()
        finally:
            cursor.close()


    def fetch_query(self, sql: str, value) -> None:
        """Execute a SELECT query and return results."""
        if self.__connection is None or not self.__connection.is_connected():
            print("Connection is not established.")
            return None

        cursor = self.__connection.cursor()
        try:
            cursor.execute(sql, value)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            cursor.close()
    
    def add_guest(self, guest_info):
        """ this will add the guest information into the guest table of the database hotel_reservation """
        
        username = guest_info["username"]
        firstname = guest_info["firstname"]
        lastname = guest_info["lastname"]
        email = guest_info["email"]
        phone = guest_info["phone"]
        address = guest_info["address"]
        birthday = guest_info["birthday"]
        
        self.__connect_db()
        try:
            sql = """
                INSERT INTO guest (username, firstname, lastname, email, phone, address, birthday)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            value = (username, firstname, lastname, email, phone, address, birthday)
            self.execute_query(sql, value)
        except Exception as e:
            print(f"Insertion error: {e}")
        
        finally:    
            self.__disconnect_db()
            print("data has been addeed")
    
    
    
'''
class Database:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.__host = host
        self.__user = user
        self.__passwd = password
        self.__database = database
        
        self.connection = None

    def connect(self):
        """Establish a connection to the database."""
        try:
            print("try to connect")
            self.connection = mysql.connector.connect(
                host= self.__host,
                user= self.__user,
                passwd= self.__passwd,
                database= self.__database
            )
            if self.connection.is_connected():
                print("Connection to the database was successful.")
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            
    def close_connection(self):
        """Close the database connection."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")
'''


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
