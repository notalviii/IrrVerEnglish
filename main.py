"""
IrrVerEnglish v1.0.0
Desktop application for learning and practising English irregular verbs.
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("IrrVerEnglish")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("IrrVerEnglish")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
