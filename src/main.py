import sys

from PySide6.QtWidgets import QApplication

from ctl_main import MainApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainApp()
    ui.show()
    sys.exit(app.exec())