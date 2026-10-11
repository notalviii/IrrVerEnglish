"""
Home page for IrrVerEnglish.
Shows an overview of the application status.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QFrame)
from PyQt6.QtCore import Qt
from typing import List
from models.verb import Verb
from utils.translations import Translations


class HomePage(QWidget):
    """Home page displaying application overview."""

    def __init__(self, settings: dict, verbs: List[Verb], language: str = 'en'):
        super().__init__()
        self.settings = settings
        self.verbs = verbs
        self.language = language
        self.init_ui()

    def init_ui(self):
        """Initialize the home page UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Welcome section
        welcome_label = QLabel(Translations.get('home_welcome', self.language))
        welcome_label.setStyleSheet("font-size: 28px; font-weight: bold;")
        layout.addWidget(welcome_label)

        description_label = QLabel(Translations.get('home_description', self.language))
        description_label.setStyleSheet("font-size: 14px; color: #666;")
        layout.addWidget(description_label)

        layout.addSpacing(30)

        # Status cards
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(20)

        # CSV file status
        csv_card, csv_value_label = self.create_status_card(
            Translations.get('home_csv_file', self.language),
            self.get_csv_status(),
            "#4CAF50"
        )
        cards_layout.addWidget(csv_card)
        self.csv_value_label = csv_value_label

        # Verbs count
        verbs_card, verbs_value_label = self.create_status_card(
            Translations.get('home_available_verbs', self.language),
            str(len(self.verbs)),
            "#2196F3"
        )
        cards_layout.addWidget(verbs_card)
        self.verbs_value_label = verbs_value_label

        # Creator
        creator_card, creator_value_label = self.create_status_card(
            Translations.get('home_creator', self.language),
            "not_alviii",
            "#FF9800"
        )
        cards_layout.addWidget(creator_card)

        layout.addLayout(cards_layout)

        layout.addSpacing(30)

        # Quick actions
        actions_label = QLabel(Translations.get('home_quick_actions', self.language))
        actions_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(actions_label)

        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(15)

        import_btn = QPushButton(Translations.get('home_import_csv', self.language))
        import_btn.clicked.connect(self.request_import)
        actions_layout.addWidget(import_btn)

        start_quiz_btn = QPushButton(Translations.get('home_start_quiz', self.language))
        start_quiz_btn.clicked.connect(self.request_start_quiz)
        actions_layout.addWidget(start_quiz_btn)

        view_verbs_btn = QPushButton(Translations.get('home_view_verbs', self.language))
        view_verbs_btn.clicked.connect(self.request_view_verbs)
        actions_layout.addWidget(view_verbs_btn)

        layout.addLayout(actions_layout)

        layout.addStretch()

    def create_status_card(self, title: str, value: str, color: str) -> tuple:
        """Create a status card widget. Returns (card, value_label)."""
        card = QFrame()
        card.setFrameStyle(QFrame.Shape.Box)
        card.setObjectName("statusCard")
        card.setStyleSheet(f"""
            QFrame#statusCard {{
                border: 2px solid {color};
                border-radius: 8px;
                background-color: transparent;
                padding: 15px;
            }}
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 12px; font-weight: bold;")
        card_layout.addWidget(title_label)

        value_label = QLabel(value)
        value_label.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {color};")
        card_layout.addWidget(value_label)

        return card, value_label

    def get_csv_status(self) -> str:
        """Get the CSV file status."""
        if len(self.verbs) == 0:
            return Translations.get('home_csv_not_loaded', self.language)
        return f"{Translations.get('home_csv_loaded', self.language)} ({len(self.verbs)} {Translations.get('verbs_verbs', self.language)})"

    def update_info(self, verbs: List[Verb]):
        """Update the displayed information."""
        self.verbs = verbs
        # Update the values directly instead of recreating UI
        self.verbs_value_label.setText(str(len(self.verbs)))
        self.csv_value_label.setText(self.get_csv_status())

    def update_settings(self, settings: dict, language: str = None):
        """Update settings."""
        self.settings = settings
        if language:
            self.language = language
        # Recreate UI to update translations
        layout = self.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.init_ui()

    def update_language(self, language: str):
        """Update language."""
        self.language = language
        # Recreate UI to update translations
        layout = self.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.init_ui()

    def request_import(self):
        """Request to import a CSV file."""
        # This will be handled by the main window
        self.parent().parent().navigate_to(2)  # Go to Verbs page

    def request_start_quiz(self):
        """Request to start a quiz."""
        self.parent().parent().navigate_to(1)  # Go to Study page

    def request_view_verbs(self):
        """Request to view verbs."""
        self.parent().parent().navigate_to(2)  # Go to Verbs page
