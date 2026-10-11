"""
Settings page for IrrVerEnglish.
Handles application configuration.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QLineEdit, QComboBox, QMessageBox)
from PyQt6.QtCore import Qt
from utils.storage import StorageManager
from utils.translations import Translations


class SettingsPage(QWidget):
    """Page for application settings."""

    def __init__(self, settings: dict, storage: StorageManager, main_window, language: str = 'en'):
        super().__init__()
        self.settings = settings
        self.storage = storage
        self.main_window = main_window
        self.language = language
        self.init_ui()

    def init_ui(self):
        """Initialize the settings page UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Title
        title_label = QLabel(Translations.get('settings_title', self.language))
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        # Theme selection
        theme_layout = QHBoxLayout()
        theme_layout.setSpacing(10)

        theme_label = QLabel(Translations.get('settings_theme', self.language) + ":")
        theme_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        theme_layout.addWidget(theme_label)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["light", "dark", "alternative", "samurai", "sunset", "forest"])
        self.theme_combo.setCurrentText(self.settings.get('theme', 'light'))
        theme_layout.addWidget(self.theme_combo)

        theme_layout.addStretch()
        layout.addLayout(theme_layout)

        # Language selection
        lang_layout = QHBoxLayout()
        lang_layout.setSpacing(10)

        lang_label = QLabel(Translations.get('settings_language', self.language) + ":")
        lang_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        lang_layout.addWidget(lang_label)

        self.lang_combo = QComboBox()
        self.lang_combo.addItem("English", "en")
        self.lang_combo.addItem("Español", "es")
        current_lang = self.settings.get('language', 'en')
        index = self.lang_combo.findData(current_lang)
        if index >= 0:
            self.lang_combo.setCurrentIndex(index)
        lang_layout.addWidget(self.lang_combo)

        lang_layout.addStretch()
        layout.addLayout(lang_layout)

        # Version info
        version_layout = QHBoxLayout()
        version_layout.setSpacing(10)

        version_label = QLabel(Translations.get('settings_version', self.language) + ":")
        version_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        version_layout.addWidget(version_label)

        version_value = QLabel("v1.0.0")
        version_value.setStyleSheet("font-size: 14px;")
        version_layout.addWidget(version_value)

        version_layout.addStretch()
        layout.addLayout(version_layout)

        layout.addSpacing(20)

        # Save button
        save_btn = QPushButton(Translations.get('settings_save', self.language))
        save_btn.clicked.connect(self.save_settings)
        save_btn.setStyleSheet("font-size: 14px; padding: 10px;")
        layout.addWidget(save_btn)

        layout.addStretch()

    def save_settings(self):
        """Save the settings."""
        theme = self.theme_combo.currentText()
        language = self.lang_combo.currentData()

        self.settings['theme'] = theme
        self.settings['language'] = language

        if self.storage.save_settings(self.settings):
            QMessageBox.information(self, Translations.get('settings_saved', self.language), Translations.get('settings_saved_msg', self.language))
            self.main_window.refresh_all()
        else:
            QMessageBox.critical(self, Translations.get('settings_error', self.language), Translations.get('settings_error_msg', self.language))

    def update_language(self, language: str):
        """Update language."""
        self.language = language
        # Recreate UI
        layout = self.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.init_ui()
