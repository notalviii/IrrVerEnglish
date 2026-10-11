"""
Statistics page for IrrVerEnglish.
Displays user performance statistics and session history.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QMessageBox, QFrame)
from PyQt6.QtCore import Qt
from utils.storage import StorageManager
from utils.translations import Translations


class StatisticsPage(QWidget):
    """Page for displaying statistics and session history."""

    def __init__(self, storage: StorageManager, language: str = 'en'):
        super().__init__()
        self.storage = storage
        self.language = language
        self.init_ui()
        self.load_statistics()

    def update_language(self, language: str):
        """Update language."""
        self.language = language
        # Recreate UI with translations
        layout = self.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.init_ui()
        self.load_statistics()

    def init_ui(self):
        """Initialize the statistics page UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Title
        title_label = QLabel(Translations.get('stats_title', self.language))
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        # Overall statistics
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(20)

        self.total_questions_card, self.total_questions_label = self.create_stat_card(Translations.get('stats_total_questions', self.language), "0", "#2196F3")
        stats_layout.addWidget(self.total_questions_card)

        self.total_correct_card, self.total_correct_label = self.create_stat_card(Translations.get('stats_total_correct', self.language), "0", "#4CAF50")
        stats_layout.addWidget(self.total_correct_card)

        self.total_incorrect_card, self.total_incorrect_label = self.create_stat_card(Translations.get('stats_total_incorrect', self.language), "0", "#f44336")
        stats_layout.addWidget(self.total_incorrect_card)

        self.accuracy_card, self.accuracy_label = self.create_stat_card(Translations.get('stats_accuracy', self.language), "0%", "#FF9800")
        stats_layout.addWidget(self.accuracy_card)

        layout.addLayout(stats_layout)

        layout.addSpacing(20)

        # Session history
        history_label = QLabel(Translations.get('stats_session_history', self.language))
        history_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(history_label)

        self.session_table = QTableWidget()
        self.session_table.setColumnCount(5)
        self.session_table.setHorizontalHeaderLabels([
            Translations.get('stats_date', self.language),
            Translations.get('stats_questions', self.language),
            Translations.get('stats_correct', self.language),
            Translations.get('stats_incorrect', self.language),
            Translations.get('stats_accuracy_header', self.language)
        ])
        self.session_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.session_table.verticalHeader().setVisible(False)
        layout.addWidget(self.session_table)

        # Reset button
        reset_btn = QPushButton(Translations.get('stats_reset', self.language))
        reset_btn.clicked.connect(self.reset_statistics)
        reset_btn.setStyleSheet("font-size: 14px; padding: 10px;")
        layout.addWidget(reset_btn)

    def create_stat_card(self, title: str, value: str, color: str) -> tuple:
        """Create a statistics card widget. Returns (card, value_label)."""
        card = QFrame()
        card.setObjectName("statCard")
        card.setStyleSheet(f"""
            QFrame#statCard {{
                border: 2px solid {color};
                border-radius: 8px;
                background-color: transparent;
                padding: 20px;
            }}
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(15)

        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        card_layout.addWidget(title_label)

        value_label = QLabel(value)
        value_label.setStyleSheet(f"font-size: 32px; font-weight: bold; color: {color};")
        card_layout.addWidget(value_label)

        return card, value_label

    def load_statistics(self):
        """Load and display statistics."""
        stats = self.storage.load_statistics()

        # Update overall statistics
        total = stats['total_questions']
        correct = stats['total_correct']
        incorrect = stats['total_incorrect']

        if total > 0:
            accuracy = (correct / total) * 100
        else:
            accuracy = 0

        self.total_questions_label.setText(str(total))
        self.total_correct_label.setText(str(correct))
        self.total_incorrect_label.setText(str(incorrect))
        self.accuracy_label.setText(f"{accuracy:.1f}%")

        # Update session history table
        self.session_table.setRowCount(len(stats['sessions']))

        for row, session in enumerate(stats['sessions']):
            self.session_table.setItem(row, 0, QTableWidgetItem(session['date']))
            self.session_table.setItem(row, 1, QTableWidgetItem(str(session['total'])))
            self.session_table.setItem(row, 2, QTableWidgetItem(str(session['correct'])))
            self.session_table.setItem(row, 3, QTableWidgetItem(str(session['incorrect'])))
            self.session_table.setItem(row, 4, QTableWidgetItem(f"{session['accuracy']:.1f}%"))

    def reset_statistics(self):
        """Reset all statistics."""
        reply = QMessageBox.question(
            self,
            Translations.get('msg_stats_confirm', self.language),
            Translations.get('msg_stats_confirm_text', self.language),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.storage.reset_statistics()
            self.load_statistics()
            QMessageBox.information(self, Translations.get('msg_stats_reset', self.language), Translations.get('msg_stats_reset_text', self.language))
