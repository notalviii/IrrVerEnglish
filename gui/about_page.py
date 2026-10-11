"""
About page for IrrVerEnglish.
Displays application information.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QFrame)
from PyQt6.QtCore import Qt
from utils.translations import Translations


class AboutPage(QWidget):
    """Page displaying application information."""

    def __init__(self, settings: dict, language: str = 'en'):
        super().__init__()
        self.settings = settings
        self.language = language
        self.init_ui()

    def update_settings(self, settings: dict, language: str = None):
        """Update settings."""
        self.settings = settings
        if language:
            self.language = language
        # Creator name is now fixed, no need to update UI

    def init_ui(self):
        """Initialize the about page UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Title
        title_label = QLabel(Translations.get('about_title', self.language))
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        # Info card
        info_card = QFrame()
        info_card.setObjectName("infoCard")
        info_card.setStyleSheet("""
            QFrame#infoCard {
                border: 2px solid #ccc;
                border-radius: 8px;
                padding: 20px;
                background-color: transparent;
            }
        """)

        card_layout = QVBoxLayout(info_card)
        card_layout.setSpacing(10)

        # Application name
        app_name_label = QLabel(f"{Translations.get('about_app_name', self.language)}: IrrVerEnglish")
        app_name_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        card_layout.addWidget(app_name_label)

        # Version
        version_label = QLabel(f"{Translations.get('about_version', self.language)}: v1.0.0")
        version_label.setStyleSheet("font-size: 14px;")
        card_layout.addWidget(version_label)

        # Description
        desc_label = QLabel(f"{Translations.get('about_description', self.language)}: {Translations.get('about_desc_text', self.language)}")
        desc_label.setStyleSheet("font-size: 14px;")
        desc_label.setWordWrap(True)
        card_layout.addWidget(desc_label)

        # Creator - Fixed to not_alviii
        creator_label = QLabel(f"{Translations.get('about_creator', self.language)}: not_alviii")
        creator_label.setStyleSheet("font-size: 14px;")
        card_layout.addWidget(creator_label)

        # Release
        release_label = QLabel(f"{Translations.get('about_release', self.language)}: {Translations.get('about_release_text', self.language)}")
        release_label.setStyleSheet("font-size: 14px;")
        card_layout.addWidget(release_label)

        layout.addWidget(info_card)

        layout.addStretch()
