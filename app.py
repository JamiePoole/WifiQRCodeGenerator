import sys
import signal

from PySide6.QtWidgets import QApplication

from widgets.windows import MainWindow

class WifiQRCodeGenerator(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        signal.signal(signal.SIGINT, signal.SIG_DFL)

        self.setApplicationName("WIFI QR Code Generator")
        self.setApplicationVersion("1.0.0")
        self.setOrganizationName("Jamie Poole")
        self.setOrganizationDomain("jamiepoole.com")

        self.main_window = MainWindow()
        self.main_window.show()
        self.setActiveWindow(self.main_window)


if __name__ == "__main__":
    app = WifiQRCodeGenerator(sys.argv)
    sys.exit(app.exec())