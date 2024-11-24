import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThreadPool, QRunnable
from landing_page import Landing
from login_page import Login
from sign_up_page import SignUp
from database import SQLConnector

class HotelStructure:
    def __init__(self):
        #self.background_run = QThreadPool()
            
        self.landing_page = Landing()
        self.login_page = Login(self.landing_page)
        self.sign_up_page = SignUp(self.landing_page, self.login_page)
        
        self.login_page.landing_page = self.landing_page
        self.landing_page.login_page = self.login_page
        self.landing_page.sign_up_page = self.sign_up_page
        
        #self.sign_up_page.register.clicked.connect(self.register_clicked)
        
        self.landing_page.show()
    
    """    
    def register_clicked(self):
        print("this gets called")
        username = self.sign_up_page.username.text().strip()
        firstname = self.sign_up_page.first_name.text().strip()
        lastname = self.sign_up_page.last_name.text().strip()
        email = self.sign_up_page.email.text().strip()
        phone = self.sign_up_page.phone.text().strip()
        address = self.sign_up_page.address.text().strip()
        birthday = self.sign_up_page.birthday.text().strip()

        this_db = SQLConnector(method= "add_guest", parameters= {
            "username": username,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "birthday": birthday
            
            }
        )
        self.background_run.start(self._run_in_background(this_db, "add_guest"))
        
        self.sign_up_page.hide()
        self.login_page.show()
        
    def _run_in_background(self, Object_to_run, method_to_run):
        "" Helper function to run an Object in background ""
        class Helper(QRunnable):
            def run(self):
                print("print helper")
                method = getattr(Object_to_run, method_to_run, None)
                if callable(method):
                    method(Object_to_run.parameters)
        return Helper()
    """

def main():
    app = QApplication(sys.argv)
    HotelStructure()

    result = app.exec_()
    sys.exit(result)

if __name__ == "__main__":
    main()
