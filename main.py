import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread
from landing_page import Landing
from login_page import Login
from sign_up_page import SignUp
from database import SQLConnector, test_database_connection

class DatabaseThread(QThread):
    def __init__(self, db_connector, sql, params):
        super(DatabaseThread, self).__init__()
        self._db_connector = db_connector
        self._sql = sql
        self._params = params
    
    def run(self):
        try:
            self._db_connector.connect()
            self._db_connector.execute_query(self._sql, self._params)
            print("seccesss")
        except:
            print("unsuccess")
        
        finally:
            self._db_connector.close_connection()
        

class HotelStructure:
    this_db = SQLConnector(
        host= "localhost",
        user= "root",
        password= "admin",
        database= "hotel_reservation"
    )
    
    def __init__(self):    
        self.landing_page = Landing()
        self.login_page = Login(self.landing_page)
        self.sign_up_page = SignUp(self.landing_page, self.login_page)
        
        self.login_page.landing_page = self.landing_page
        self.landing_page.login_page = self.login_page
        self.landing_page.sign_up_page = self.sign_up_page
        test_database_connection() # uncomment this to show the real error
        
        self.landing_page.show()
        
        self.sign_up_page.register.clicked.connect(self.register_clicked)
    
    
    def register_clicked(self):
        print("this gets called")
        username = self.sign_up_page.username.text().strip()
        firstname = self.sign_up_page.first_name.text().strip()
        lastname = self.sign_up_page.last_name.text().strip()
        email = self.sign_up_page.email.text().strip()
        phone = self.sign_up_page.phone.text().strip()
        address = self.sign_up_page.address.text().strip()
        birthday = self.sign_up_page.birthday.text().strip()
        
        sql = """
            INSERT INTO guest (username, firstname, lastname, email, phone, address, birthday)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        params = (username, firstname, lastname, email, phone, address, birthday)

        db_thread = DatabaseThread(HotelStructure.this_db, sql, params)

        db_thread.start()
        
        self.sign_up_page.hide()
        self.login_page.show()
'''
        try:
            HotelStructure.this_db.execute_query(sql, params)
            print("User registered successfully.")
        except Exception as e:
            print(f"Error during registration: {e}")
        finally:
            HotelStructure.this_db.close_connection()
        
'''        
        #self.this_db.add_guest(username, firstname, lastname, email, phone, address, birthday)
        
        # Switch to login page after registration
        


def main():
    app = QApplication(sys.argv)
    hotel = HotelStructure()

    
    result = app.exec_()
    sys.exit(result)


if __name__ == "__main__":
    main()
