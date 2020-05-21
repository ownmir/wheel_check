import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QHBoxLayout
from db.db_simple import connect_to_base_and_execute


class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.ok_button = QPushButton("Run")
        self.user_entry = QLineEdit("user5301")
        self.pass_entry = QLineEdit("d")
        self.horizontal_box = QHBoxLayout()

        self.init_ui()

    def init_ui(self):
        self.pass_entry.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.horizontal_box.addWidget(self.ok_button)
        self.horizontal_box.addWidget(self.user_entry)
        self.horizontal_box.addWidget(self.pass_entry)
        query = "SELECT column_name FROM ALL_TAB_COLUMNS WHERE table_name = :table_name"
        self.ok_button.clicked.connect(
            lambda: connect_to_base_and_execute(query, self.user_entry.text(), self.pass_entry.text(), 'DK')
        )
        self.setLayout(self.horizontal_box)

        self.setGeometry(300, 100, 550, 150)
        self.setWindowTitle('Simple db')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
