"""
Theme definitions for IrrVerEnglish.
Provides color schemes with gradients and visual enhancements.
"""

from PyQt6.QtGui import QColor, QPalette, QLinearGradient
from PyQt6.QtCore import Qt


class Theme:
    """Base theme class."""

    def __init__(self, name: str):
        self.name = name

    def get_palette(self) -> QPalette:
        """Return the color palette for this theme."""
        raise NotImplementedError


class LightTheme(Theme):
    """Light theme with gradient backgrounds."""

    def __init__(self):
        super().__init__("light")

    def get_palette(self) -> QPalette:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(245, 247, 250))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(33, 37, 41))
        palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(248, 249, 252))
        palette.setColor(QPalette.ColorRole.Text, QColor(33, 37, 41))
        palette.setColor(QPalette.ColorRole.Button, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(33, 37, 41))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(220, 53, 69))
        palette.setColor(QPalette.ColorRole.Link, QColor(13, 110, 253))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(13, 110, 253))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        return palette

    def get_stylesheet(self) -> str:
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #f5f7fa, stop:1 #c3cfe2);
            }
            QWidget {
                background-color: transparent;
                color: #212529;
            }
            QFrame {
                background-color: transparent;
                color: #212529;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ffffff, stop:1 #e9ecef);
                border: 1px solid #dee2e6;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: 500;
                color: #212529;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #e9ecef, stop:1 #dee2e6);
                color: #212529;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #dee2e6, stop:1 #ced4da);
                color: #212529;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #dee2e6;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                color: #212529;
            }
            QLineEdit:focus {
                border-color: #0d6efd;
                color: #212529;
            }
            QTableWidget {
                background-color: #ffffff;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                gridline-color: #e9ecef;
                color: #212529;
            }
            QTableWidget::item {
                padding: 8px;
                color: #212529;
            }
            QTableWidget::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0d6efd, stop:1 #0056b3);
                color: #ffffff;
            }
            QTableWidget::horizontalHeader {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f8f9fa, stop:1 #e9ecef);
                border: none;
                border-bottom: 2px solid #dee2e6;
                padding: 8px;
                color: #212529;
            }
            QLabel {
                color: #212529;
            }
            QTabWidget::pane {
                border: 2px solid #dee2e6;
                border-radius: 8px;
                background-color: #ffffff;
                color: #212529;
            }
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f8f9fa, stop:1 #e9ecef);
                padding: 10px 20px;
                border: 2px solid #dee2e6;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
                color: #212529;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ffffff, stop:1 #f8f9fa);
                border-bottom: 2px solid #ffffff;
                color: #212529;
            }
        """


class DarkTheme(Theme):
    """Dark theme with gradient backgrounds."""

    def __init__(self):
        super().__init__("dark")

    def get_palette(self) -> QPalette:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 100, 100))
        palette.setColor(QPalette.ColorRole.Link, QColor(100, 180, 255))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(100, 180, 255))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
        return palette

    def get_stylesheet(self) -> str:
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a2e, stop:0.5 #16213e, stop:1 #0f3460);
            }
            QWidget {
                background-color: transparent;
                color: #ffffff;
            }
            QFrame {
                background-color: transparent;
                color: #ffffff;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #4a4a4a, stop:1 #2a2a2a);
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: 500;
                color: #ffffff;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #5a5a5a, stop:1 #3a3a3a);
                border-color: #777777;
                color: #ffffff;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3a3a3a, stop:1 #2a2a2a);
                color: #ffffff;
            }
            QLineEdit {
                background-color: #2a2a2a;
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                color: #ffffff;
            }
            QLineEdit:focus {
                border-color: #64b5f6;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #2a2a2a;
                border: 2px solid #555555;
                border-radius: 8px;
                gridline-color: #3a3a3a;
                color: #ffffff;
            }
            QTableWidget::item {
                padding: 8px;
                color: #ffffff;
            }
            QTableWidget::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #64b5f6, stop:1 #1976d2);
                color: #ffffff;
            }
            QTableWidget::horizontalHeader {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3a3a3a, stop:1 #2a2a2a);
                border: none;
                border-bottom: 2px solid #555555;
                padding: 8px;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QTabWidget::pane {
                border: 2px solid #555555;
                border-radius: 8px;
                background-color: #2a2a2a;
                color: #ffffff;
            }
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3a3a3a, stop:1 #2a2a2a);
                padding: 10px 20px;
                border: 2px solid #555555;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
                color: #ffffff;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a2a2a, stop:1 #3a3a3a);
                border-bottom: 2px solid #2a2a2a;
                color: #ffffff;
            }
        """


class AlternativeTheme(Theme):
    """Alternative theme with vibrant gradient colors."""

    def __init__(self):
        super().__init__("alternative")

    def get_palette(self) -> QPalette:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(240, 248, 255))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(44, 62, 80))
        palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(230, 240, 255))
        palette.setColor(QPalette.ColorRole.Text, QColor(44, 62, 80))
        palette.setColor(QPalette.ColorRole.Button, QColor(52, 152, 219))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(231, 76, 60))
        palette.setColor(QPalette.ColorRole.Link, QColor(41, 128, 185))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(52, 152, 219))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        return palette

    def get_stylesheet(self) -> str:
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
            }
            QWidget {
                background-color: transparent;
                color: #2c3e50;
            }
            QFrame {
                background-color: transparent;
                color: #2c3e50;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3498db, stop:1 #2980b9);
                border: 2px solid #2980b9;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: 500;
                color: #ffffff;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #5dade2, stop:1 #3498db);
                color: #ffffff;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2980b9, stop:1 #1a5276);
                color: #ffffff;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #3498db;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border-color: #1a5276;
                color: #2c3e50;
            }
            QTableWidget {
                background-color: #ffffff;
                border: 2px solid #3498db;
                border-radius: 8px;
                gridline-color: #d6eaf8;
                color: #2c3e50;
            }
            QTableWidget::item {
                padding: 8px;
                color: #2c3e50;
            }
            QTableWidget::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498db, stop:1 #1a5276);
                color: #ffffff;
            }
            QTableWidget::horizontalHeader {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ecf0f1, stop:1 #bdc3c7);
                border: none;
                border-bottom: 2px solid #3498db;
                padding: 8px;
                color: #2c3e50;
            }
            QLabel {
                color: #2c3e50;
            }
            QTabWidget::pane {
                border: 2px solid #3498db;
                border-radius: 8px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ecf0f1, stop:1 #bdc3c7);
                padding: 10px 20px;
                border: 2px solid #3498db;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
                color: #2c3e50;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ffffff, stop:1 #ecf0f1);
                border-bottom: 2px solid #ffffff;
                color: #2c3e50;
            }
        """


class SamuraiTheme(Theme):
    """Japanese Samurai theme - black and white inspired by ancient warriors."""

    def __init__(self):
        super().__init__("samurai")

    def get_palette(self) -> QPalette:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(20, 20, 20))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(200, 200, 200))
        palette.setColor(QPalette.ColorRole.Link, QColor(180, 180, 180))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(100, 100, 100))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        return palette

    def get_stylesheet(self) -> str:
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0a0a0a, stop:0.5 #1a1a1a, stop:1 #0f0f0f);
            }
            QWidget {
                background-color: transparent;
                color: #ffffff;
            }
            QFrame {
                background-color: transparent;
                color: #ffffff;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3a3a3a, stop:1 #1a1a1a);
                border: 2px solid #ffffff;
                border-radius: 4px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: bold;
                color: #ffffff;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #4a4a4a, stop:1 #2a2a2a);
                border-color: #cccccc;
                color: #ffffff;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a2a2a, stop:1 #1a1a1a);
                color: #ffffff;
            }
            QLineEdit {
                background-color: #1a1a1a;
                border: 2px solid #ffffff;
                border-radius: 4px;
                padding: 8px;
                font-size: 13px;
                color: #ffffff;
            }
            QLineEdit:focus {
                border-color: #888888;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #1a1a1a;
                border: 2px solid #ffffff;
                border-radius: 4px;
                gridline-color: #2a2a2a;
                color: #ffffff;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #2a2a2a;
                color: #ffffff;
            }
            QTableWidget::item:selected {
                background-color: #4a4a4a;
                color: #ffffff;
                border: 1px solid #ffffff;
            }
            QTableWidget::horizontalHeader {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a2a2a, stop:1 #1a1a1a);
                border: none;
                border-bottom: 2px solid #ffffff;
                padding: 8px;
                color: #ffffff;
                font-weight: bold;
            }
            QLabel {
                color: #ffffff;
            }
            QTabWidget::pane {
                border: 2px solid #ffffff;
                border-radius: 4px;
                background-color: #1a1a1a;
                color: #ffffff;
            }
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a2a2a, stop:1 #1a1a1a);
                padding: 10px 20px;
                border: 2px solid #ffffff;
                border-bottom: none;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                margin-right: 2px;
                color: #ffffff;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #2a2a2a);
                border-bottom: 2px solid #1a1a1a;
                color: #ffffff;
            }
        """


class SunsetTheme(Theme):
    """Sunset theme with warm gradient colors."""

    def __init__(self):
        super().__init__("sunset")

    def get_palette(self) -> QPalette:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(45, 25, 35))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(60, 30, 45))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(70, 40, 55))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(230, 100, 50))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 200, 100))
        palette.setColor(QPalette.ColorRole.Link, QColor(255, 150, 100))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(230, 100, 50))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        return palette

    def get_stylesheet(self) -> str:
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #2d1917, stop:0.5 #4a2c2a, stop:1 #6b3a3a);
            }
            QWidget {
                background-color: transparent;
                color: #ffffff;
            }
            QFrame {
                background-color: transparent;
                color: #ffffff;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #e67e22, stop:1 #d35400);
                border: 2px solid #e67e22;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: 500;
                color: #ffffff;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f39c12, stop:1 #e67e22);
                color: #ffffff;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #d35400, stop:1 #a04000);
                color: #ffffff;
            }
            QLineEdit {
                background-color: #3a2020;
                border: 2px solid #e67e22;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                color: #ffffff;
            }
            QLineEdit:focus {
                border-color: #f39c12;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #3a2020;
                border: 2px solid #e67e22;
                border-radius: 8px;
                gridline-color: #4a2a2a;
                color: #ffffff;
            }
            QTableWidget::item {
                padding: 8px;
                color: #ffffff;
            }
            QTableWidget::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #e67e22, stop:1 #d35400);
                color: #ffffff;
            }
            QTableWidget::horizontalHeader {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #4a2a2a, stop:1 #3a2020);
                border: none;
                border-bottom: 2px solid #e67e22;
                padding: 8px;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QTabWidget::pane {
                border: 2px solid #e67e22;
                border-radius: 8px;
                background-color: #3a2020;
                color: #ffffff;
            }
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #4a2a2a, stop:1 #3a2020);
                padding: 10px 20px;
                border: 2px solid #e67e22;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
                color: #ffffff;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3a2020, stop:1 #4a2a2a);
                border-bottom: 2px solid #3a2020;
                color: #ffffff;
            }
        """


class ForestTheme(Theme):
    """Forest theme with natural green gradients."""

    def __init__(self):
        super().__init__("forest")

    def get_palette(self) -> QPalette:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(20, 40, 25))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(30, 50, 35))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(40, 60, 45))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(76, 175, 80))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(129, 199, 132))
        palette.setColor(QPalette.ColorRole.Link, QColor(102, 187, 106))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(76, 175, 80))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        return palette

    def get_stylesheet(self) -> str:
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1b5e20, stop:0.5 #2e7d32, stop:1 #388e3c);
            }
            QWidget {
                background-color: transparent;
                color: #ffffff;
            }
            QFrame {
                background-color: transparent;
                color: #ffffff;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #4caf50, stop:1 #388e3c);
                border: 2px solid #4caf50;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: 500;
                color: #ffffff;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #66bb6a, stop:1 #4caf50);
                color: #ffffff;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #388e3c, stop:1 #1b5e20);
                color: #ffffff;
            }
            QLineEdit {
                background-color: #1e3a28;
                border: 2px solid #4caf50;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                color: #ffffff;
            }
            QLineEdit:focus {
                border-color: #66bb6a;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #1e3a28;
                border: 2px solid #4caf50;
                border-radius: 8px;
                gridline-color: #2a4a35;
                color: #ffffff;
            }
            QTableWidget::item {
                padding: 8px;
                color: #ffffff;
            }
            QTableWidget::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4caf50, stop:1 #1b5e20);
                color: #ffffff;
            }
            QTableWidget::horizontalHeader {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a4a35, stop:1 #1e3a28);
                border: none;
                border-bottom: 2px solid #4caf50;
                padding: 8px;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QTabWidget::pane {
                border: 2px solid #4caf50;
                border-radius: 8px;
                background-color: #1e3a28;
                color: #ffffff;
            }
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a4a35, stop:1 #1e3a28);
                padding: 10px 20px;
                border: 2px solid #4caf50;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
                color: #ffffff;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1e3a28, stop:1 #2a4a35);
                border-bottom: 2px solid #1e3a28;
                color: #ffffff;
            }
        """


def get_theme(theme_name: str) -> Theme:
    """Get a theme by name."""
    themes = {
        'light': LightTheme(),
        'dark': DarkTheme(),
        'alternative': AlternativeTheme(),
        'samurai': SamuraiTheme(),
        'sunset': SunsetTheme(),
        'forest': ForestTheme()
    }
    return themes.get(theme_name, LightTheme())
