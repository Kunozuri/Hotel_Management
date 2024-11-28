from PyQt5.QtWidgets import (
    QApplication, QTableWidgetItem, QSizePolicy, QLineEdit, QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QHeaderView, QTableWidget
)
from PyQt5.QtCore import Qt, QThreadPool
from database import SQLConnector
from sign_up_page import SignUp

class Admin(QWidget):
    def __init__(self, landing_page: object= None, parent= None):
        super(Admin, self).__init__(parent= None)
        
        self.current_table = "reservation"
        self.background_run = QThreadPool()
        
        self.__landing_page = landing_page
        self.to_run_in_background = SignUp
        
        self.settings()
        self.initUI()

    def initUI(self) -> None:
        master_layout = QVBoxLayout()
        
        row01 = self.app_bar()
        row02 = QHBoxLayout()
        
        navigation = QPushButton(f"{"View Transactions" if self.current_table == "reservation" else "Back"}")
        edit = QPushButton("Edit")
        
        table = self.table_on_display()
        
        heads = table.horizontalHeader()
        heads.sectionClicked.connect(self.headers)

        row02.addWidget(navigation)
        row02.addWidget(edit)
        
        master_layout.addWidget(row01)
        master_layout.addLayout(row02)
        master_layout.addWidget(table)
        
        self.setLayout(master_layout)
    
    def app_bar(self) -> QWidget:
        app_bar = QWidget()
        app_bar.setMinimumSize(1360, 150)
        app_bar.setStyleSheet("""
        background-color: #cccccc;
        border-radius: 20px;
        """)
        
        master_layout = QVBoxLayout(app_bar)
        row01 = QHBoxLayout()
        row02 = QHBoxLayout()
        
        logo = QLabel("Zrsmyley")
        logout = QPushButton("Logout")
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText(f"Search the {self.current_table} {"username" if self.current_table == "guest" else "ID"}")
        
        search = QPushButton("Search")
        
        logout.clicked.connect(self.logout)
        search.clicked.connect(self.search)
        
        row01.addWidget(logo)
        row01.addWidget(logout)
        row02.addWidget(self.search_bar)
        row02.addWidget(search)
        
        master_layout.addLayout(row01)
        master_layout.addLayout(row02)
        
        return app_bar
        
    def tables(self, table_name) -> QTableWidget:
        """ this create the table and populate it directly """
        
        # This area needs to debug in other device TAKE NOTE!
        """
        # -- getting data from database  -- #
        this_db = SQLConnector(method= "get_table_content", parameters= table_name)
        table_content = self.to_run_in_background.run_in_background(None, this_db, this_db.method)
        self.background_run.start(table_content)
        print(table_content.result)
        data, table_header = table_content.result
        """
        # -- displaying header into table -- #
        table = QTableWidget(0,1) # len(table_header)
        table.setHorizontalHeaderLabels(['hello']) # table_header
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)    
        """
        # -- displaying data into table -- #
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        """
        return table

# -- SYSTEM -- #
    def settings(self) -> None:
        self.setWindowTitle("zrsmyley -- Admin")
        self.setGeometry(100, 100, 1366, 768)

# -- EVENTS -- #
    def logout(self) -> None:
        self.hide()
        self.__landing_page.show()

    def search(self) -> None:
        from_this = "username" if self.current_table == "guest" else f"{self.current_table}_id"
        look_for = self.search_bar.text()
        
        this_db = SQLConnector(method= "get_searched", parameters= {"from_this": from_this, "look_for": look_for})
        table_content = self.to_run_in_background.run_in_background(None, this_db, this_db.method)
        self.background_run.start(table_content)
        
# -- CONTROL FLOW EVENTS -- #
    def navigation(self) -> None:
        match self.current_table:
            case "reservation":
                self.current_table = "transaction"
            case "transaction":
                self.current_table = "reservation"
            case "guest":
                self.current_table = "reservation"
            case "auth":
                self.current_table = "guest"
            case "room":
                self.current_table = "reservation"

    def headers(self, index: int) -> None:
        match self.current_table:
            case "reservation":
                match index:
                    case 1:
                        self.current_table = "guest"
                    case 2:
                        self.current_table = "room"
            case "guest":
                match index:
                    case 1:
                        self.current_table = "auth"
            case "transaction":
                match index:
                    case 1:
                        self.current_table = "reservation" 

    def table_on_display(self) -> QTableWidget:
        """ helper that will switches between the current displayed table """
        match self.current_table:
            case "reservation":
                table = self.tables("reservation")
            case "guest":
                table = self.tables("guest")
            case "room":
                table = self.tables("room")
            case "auth":
                table = self.tables("authentication")
            case "transaction":
                table = self.tables("transaction")
        return table
    """ ATTENTION: if not works on changing the table then try this inserting inside the button clicked functions"""

# -- HELPERS -- #   
    def populate_table(self, data):
        # -- displaying header into table -- #
        table = QTableWidget(1,) # len(table_header)
        table.setHorizontalHeaderLabels(['hello']) # table_header
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)    
        
        # -- displaying data into table -- #
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Show the main window
    window = Admin()
    window.show()

    sys.exit(app.exec_())