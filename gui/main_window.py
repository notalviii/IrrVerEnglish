"""
Main window for IrrVerEnglish.
Contains the navigation and all sections of the application.
"""

from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QStackedWidget, QLabel, QPushButton)
from PyQt6.QtCore import Qt
from utils.storage import StorageManager
from utils.themes import get_theme
from utils.translations import Translations
from gui.home_page import HomePage
from gui.study_page import StudyPage
from gui.verbs_page import VerbsPage
from gui.statistics_page import StatisticsPage
from gui.settings_page import SettingsPage
from gui.about_page import AboutPage


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()
        self.storage = StorageManager()
        self.settings = self.storage.load_settings()
        self.language = self.settings.get('language', 'en')
        self.verbs = []
        self.selected_verbs = []

        self.setWindowTitle("IrrVerEnglish v1.0.0")
        self.setMinimumSize(1000, 700)

        self.init_ui()
        self.apply_theme()
        self.apply_language()

    def init_ui(self):
        """Initialize the user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create navigation sidebar
        nav_widget = self.create_navigation()
        main_layout.addWidget(nav_widget)

        # Create content area
        self.content_stack = QStackedWidget()
        main_layout.addWidget(self.content_stack, stretch=1)

        # Create pages
        self.home_page = HomePage(self.settings, self.verbs, self.language)
        self.study_page = StudyPage(self.verbs, self.selected_verbs, self.storage, self.language)
        self.verbs_page = VerbsPage(self.verbs, self.selected_verbs, self.study_page, self.language)
        self.statistics_page = StatisticsPage(self.storage, self.language)
        self.settings_page = SettingsPage(self.settings, self.storage, self, self.language)
        self.about_page = AboutPage(self.settings, self.language)

        self.content_stack.addWidget(self.home_page)
        self.content_stack.addWidget(self.study_page)
        self.content_stack.addWidget(self.verbs_page)
        self.content_stack.addWidget(self.statistics_page)
        self.content_stack.addWidget(self.settings_page)
        self.content_stack.addWidget(self.about_page)

    def create_navigation(self):
        """Create the navigation sidebar."""
        nav_widget = QWidget()
        nav_widget.setFixedWidth(200)
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setContentsMargins(10, 20, 10, 20)
        nav_layout.setSpacing(5)

        # App title
        title_label = QLabel("IrrVerEnglish")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        nav_layout.addWidget(title_label)

        nav_layout.addSpacing(20)

        # Navigation buttons
        self.nav_buttons = []

        pages = [
            ("nav_home", 0),
            ("nav_study", 1),
            ("nav_verbs", 2),
            ("nav_statistics", 3),
            ("nav_settings", 4),
            ("nav_about", 5)
        ]

        for key, index in pages:
            btn = QPushButton(Translations.get(key, self.language))
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, idx=index: self.navigate_to(idx))
            nav_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        nav_layout.addStretch()

        return nav_widget

    def navigate_to(self, index: int):
        """Navigate to a specific page."""
        self.content_stack.setCurrentIndex(index)

        # Update button states
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)

        # Refresh pages when navigating
        if index == 0:  # Home
            self.home_page.update_info(self.verbs)
        elif index == 2:  # Verbs
            self.verbs_page.refresh_verb_list()
        elif index == 3:  # Statistics
            self.statistics_page.load_statistics()

    def apply_theme(self):
        """Apply the selected theme."""
        theme_name = self.settings.get('theme', 'light')
        theme = get_theme(theme_name)
        self.setPalette(theme.get_palette())
        self.setStyleSheet(theme.get_stylesheet())

    def apply_language(self):
        """Apply the selected language."""
        self.language = self.settings.get('language', 'en')
        # Update navigation buttons
        pages = [
            ("nav_home", 0),
            ("nav_study", 1),
            ("nav_verbs", 2),
            ("nav_statistics", 3),
            ("nav_settings", 4),
            ("nav_about", 5)
        ]
        for i, (key, index) in enumerate(pages):
            self.nav_buttons[i].setText(Translations.get(key, self.language))

    def update_verbs(self, verbs):
        """Update the verbs list across all pages."""
        self.verbs = verbs
        self.home_page.update_info(verbs)
        self.verbs_page.update_verbs(verbs)
        self.study_page.update_verbs(verbs)

    def update_selected_verbs(self, selected_verbs):
        """Update the selected verbs list."""
        self.selected_verbs = selected_verbs
        self.study_page.update_selected_verbs(selected_verbs)

    def refresh_all(self):
        """Refresh all pages after settings change."""
        self.settings = self.storage.load_settings()
        self.apply_theme()
        self.apply_language()
        self.home_page.update_settings(self.settings, self.language)
        self.about_page.update_settings(self.settings, self.language)
        self.verbs_page.update_language(self.language)
        self.statistics_page.update_language(self.language)
        self.study_page.update_language(self.language)
