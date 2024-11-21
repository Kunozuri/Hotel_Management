from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QDateEdit
from PyQt5.QtCore import Qt

class SignUp(QWidget):
    def __init__(self, landing_page: object=None, login_page: object=None, parent:object = None):
        super(SignUp, self).__init__(parent)

        self.landing_page = landing_page
        self.login_page = login_page
        
        self.settings()
        self.initUI()
        
    
    def initUI(self):
        master_layout = QVBoxLayout()
        r0w1 = QHBoxLayout()
        
        logo = self.landing_page.button001(font="Lato")
        back_button = self.login_page.back_button()
        
        back_button.clicked.connect(self.back_button_clicked)
        
        self.username = self.landing_page.input_box("Username", bg_color="#FFFFFF", width= 500, height=70)
        self.first_name = self.landing_page.input_box("Firstname", bg_color="#FFFFFF", width= 500, height=70)
        self.last_name = self.landing_page.input_box("Lastname", bg_color="#FFFFFF", width= 500, height=70)
        self.email = self.landing_page.input_box("Email", bg_color="#FFFFFF", width= 500, height=70)
        self.phone = self.landing_page.input_box("Phone", bg_color="#FFFFFF", width= 500, height=70)
        self.address = self.landing_page.input_box("Address", bg_color="#FFFFFF", width= 500, height=70)
        self.birthday = self.landing_page.input_box("Birthday", bg_color="#FFFFFF", width= 500, height=70)
        
        self.register = self.landing_page.button002(text="Register", bg_color="#000000", text_color="white")


        r0w1.addWidget(back_button)
        r0w1.addWidget(logo)

        master_layout.addLayout(r0w1)
        master_layout.addWidget(self.username, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addWidget(self.first_name, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addWidget(self.last_name, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addWidget(self.phone, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addWidget(self.address, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addWidget(self.birthday, alignment=Qt.AlignmentFlag.AlignCenter)
        
        master_layout.addWidget(self.register, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(master_layout)
        
        
        
        
    
    def settings(self):
        self.setWindowTitle("zrsmyley--Landing Page")
        self.setGeometry(100, 100, 1366, 768)
    
    def back_button_clicked(self):
        self.hide()
        self.landing_page.show()
    
        
    