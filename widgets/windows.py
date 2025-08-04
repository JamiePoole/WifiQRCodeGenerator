from PySide6.QtWidgets import QGroupBox, QLabel, QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WIFI QR Code Generator")
        self.setGeometry(100, 100, 800, 600)

        content = QWidget()
        layout = QVBoxLayout(content)
        
        self.setCentralWidget(content)
        content.setLayout(layout)

        group_box = QGroupBox("QR Code")
        group_layout = QVBoxLayout()
        welcome_label = QLabel("Welcome to the WIFI QR Code Generator!")
        group_layout.addWidget(welcome_label)
        group_box.setLayout(group_layout)
        group_box.setVisible(True)

        layout.addWidget(group_box)