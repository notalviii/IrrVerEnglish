"""
Verbs page for IrrVerEnglish.
Handles CSV import and verb selection.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QLineEdit, QFileDialog, QMessageBox,
                             QSpinBox, QDialog, QDialogButtonBox)
from PyQt6.QtCore import Qt
from typing import List
from models.verb import Verb
from utils.csv_importer import CSVImporter
from utils.translations import Translations


class VerbsPage(QWidget):
    """Page for importing and selecting verbs."""

    def __init__(self, verbs: List[Verb], selected_verbs: List[Verb], study_page, language: str = 'en'):
        super().__init__()
        self.verbs = verbs
        self.selected_verbs = selected_verbs
        self.study_page = study_page
        self.language = language
        self.init_ui()

    def init_ui(self):
        """Initialize the verbs page UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Title
        title_label = QLabel(Translations.get('verbs_title', self.language))
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        # Import section
        import_layout = QHBoxLayout()
        import_layout.setSpacing(10)

        import_btn = QPushButton(Translations.get('verbs_import', self.language))
        import_btn.clicked.connect(self.import_csv)
        import_layout.addWidget(import_btn)

        self.verb_count_label = QLabel(f"{Translations.get('verbs_loaded', self.language)}: {len(self.verbs)} {Translations.get('verbs_verbs', self.language)}")
        import_layout.addWidget(self.verb_count_label)

        import_layout.addStretch()
        layout.addLayout(import_layout)

        # Selection controls
        selection_layout = QHBoxLayout()
        selection_layout.setSpacing(10)

        select_all_btn = QPushButton(Translations.get('verbs_select_all', self.language))
        select_all_btn.clicked.connect(self.select_all)
        selection_layout.addWidget(select_all_btn)

        deselect_all_btn = QPushButton(Translations.get('verbs_deselect_all', self.language))
        deselect_all_btn.clicked.connect(self.deselect_all)
        selection_layout.addWidget(deselect_all_btn)

        invert_btn = QPushButton(Translations.get('verbs_invert', self.language))
        invert_btn.clicked.connect(self.invert_selection)
        selection_layout.addWidget(invert_btn)

        range_btn = QPushButton(Translations.get('verbs_range', self.language))
        range_btn.clicked.connect(self.select_by_range)
        selection_layout.addWidget(range_btn)

        selection_layout.addStretch()

        self.selected_count_label = QLabel(f"{Translations.get('verbs_selected', self.language)}: 0 {Translations.get('verbs_verbs', self.language)}")
        selection_layout.addWidget(self.selected_count_label)

        layout.addLayout(selection_layout)

        # Search
        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)

        search_label = QLabel(Translations.get('verbs_search', self.language) + ":")
        search_layout.addWidget(search_label)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(Translations.get('verbs_search_placeholder', self.language))
        self.search_input.textChanged.connect(self.filter_verbs)
        search_layout.addWidget(self.search_input)

        layout.addLayout(search_layout)

        # Verb table
        self.verb_table = QTableWidget()
        self.verb_table.setColumnCount(6)
        self.verb_table.setHorizontalHeaderLabels([
            Translations.get('verbs_select_header', self.language),
            Translations.get('verbs_row_header', self.language),
            Translations.get('verbs_infinitive_header', self.language),
            Translations.get('verbs_past_simple_header', self.language),
            Translations.get('verbs_past_participle_header', self.language),
            Translations.get('verbs_spanish_header', self.language)
        ])
        self.verb_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.verb_table.verticalHeader().setVisible(False)
        self.verb_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        layout.addWidget(self.verb_table)

        # Start quiz button
        start_quiz_btn = QPushButton(Translations.get('verbs_start_quiz', self.language))
        start_quiz_btn.clicked.connect(self.start_quiz)
        start_quiz_btn.setStyleSheet("font-size: 14px; padding: 10px;")
        layout.addWidget(start_quiz_btn)

        self.refresh_verb_list()

    def import_csv(self):
        """Import verbs from a CSV file."""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Select CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )

        if file_path:
            importer = CSVImporter()
            verbs, errors = importer.import_csv(file_path)

            if errors:
                error_msg = "Errors encountered:\n\n" + "\n".join(errors)
                QMessageBox.warning(self, "Import Errors", error_msg)

            if verbs:
                self.verbs = verbs
                self.selected_verbs = []
                self.refresh_verb_list()
                self.verb_count_label.setText(f"{Translations.get('verbs_loaded', self.language)}: {len(self.verbs)} {Translations.get('verbs_verbs', self.language)}")

                # Update study page
                self.study_page.update_verbs(verbs)
                self.study_page.update_selected_verbs([])

                QMessageBox.information(
                    self,
                    Translations.get('msg_import_success', self.language),
                    f"{Translations.get('msg_import_success_text', self.language)} {len(verbs)} {Translations.get('verbs_verbs', self.language)}."
                )
            else:
                QMessageBox.critical(
                    self,
                    Translations.get('msg_import_error', self.language),
                    Translations.get('msg_import_error_text', self.language)
                )

    def refresh_verb_list(self):
        """Refresh the verb table."""
        self.verb_table.setRowCount(len(self.verbs))

        for row, verb in enumerate(self.verbs):
            # Checkbox for selection
            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            checkbox_item.setCheckState(Qt.CheckState.Checked if verb in self.selected_verbs else Qt.CheckState.Unchecked)
            self.verb_table.setItem(row, 0, checkbox_item)

            # Row number
            self.verb_table.setItem(row, 1, QTableWidgetItem(str(verb.row_number)))

            # Verb forms
            self.verb_table.setItem(row, 2, QTableWidgetItem(verb.infinitive))
            self.verb_table.setItem(row, 3, QTableWidgetItem(verb.past_simple))
            self.verb_table.setItem(row, 4, QTableWidgetItem(verb.past_participle))
            self.verb_table.setItem(row, 5, QTableWidgetItem(verb.spanish_translation))

        self.update_selected_count()

        # Connect checkbox changes
        self.verb_table.itemChanged.connect(self.on_item_changed)

    def on_item_changed(self, item):
        """Handle item changes in the table."""
        if item.column() == 0:  # Checkbox column
            row = item.row()
            verb = self.verbs[row]

            if item.checkState() == Qt.CheckState.Checked:
                if verb not in self.selected_verbs:
                    self.selected_verbs.append(verb)
            else:
                if verb in self.selected_verbs:
                    self.selected_verbs.remove(verb)

            self.update_selected_count()

    def select_all(self):
        """Select all verbs."""
        self.selected_verbs = self.verbs.copy()
        self.refresh_verb_list()

    def deselect_all(self):
        """Deselect all verbs."""
        self.selected_verbs = []
        self.refresh_verb_list()

    def invert_selection(self):
        """Invert the current selection."""
        self.selected_verbs = [v for v in self.verbs if v not in self.selected_verbs]
        self.refresh_verb_list()

    def select_by_range(self):
        """Select verbs by row range."""
        if not self.verbs:
            QMessageBox.warning(self, Translations.get('msg_no_verbs', self.language), Translations.get('msg_no_verbs_text', self.language))
            return

        dialog = QDialog(self)
        dialog.setWindowTitle(Translations.get('msg_range_title', self.language))
        dialog_layout = QVBoxLayout(dialog)

        # Start row
        start_layout = QHBoxLayout()
        start_layout.addWidget(QLabel(Translations.get('msg_range_start', self.language) + ":"))
        start_spin = QSpinBox()
        start_spin.setRange(1, len(self.verbs))
        start_spin.setValue(1)
        start_layout.addWidget(start_spin)
        dialog_layout.addLayout(start_layout)

        # End row
        end_layout = QHBoxLayout()
        end_layout.addWidget(QLabel(Translations.get('msg_range_end', self.language) + ":"))
        end_spin = QSpinBox()
        end_spin.setRange(1, len(self.verbs))
        end_spin.setValue(len(self.verbs))
        end_layout.addWidget(end_spin)
        dialog_layout.addLayout(end_layout)

        # Buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        dialog_layout.addWidget(buttons)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            start = start_spin.value()
            end = end_spin.value()

            if start > end:
                QMessageBox.warning(self, Translations.get('msg_range_invalid', self.language), Translations.get('msg_range_invalid_text', self.language))
                return

            # Select verbs in range
            for verb in self.verbs:
                if start <= verb.row_number <= end:
                    if verb not in self.selected_verbs:
                        self.selected_verbs.append(verb)

            self.refresh_verb_list()

    def filter_verbs(self, text: str):
        """Filter verbs based on search text."""
        search_text = text.lower()

        for row in range(self.verb_table.rowCount()):
            verb = self.verbs[row]
            forms = verb.get_forms()
            match = any(search_text in form.lower() for form in forms)
            self.verb_table.setRowHidden(row, not match)

    def update_selected_count(self):
        """Update the selected count label."""
        self.selected_count_label.setText(f"{Translations.get('verbs_selected', self.language)}: {len(self.selected_verbs)} {Translations.get('verbs_verbs', self.language)}")

    def start_quiz(self):
        """Start a quiz with selected verbs."""
        if not self.selected_verbs:
            QMessageBox.warning(self, Translations.get('msg_no_selection', self.language), Translations.get('msg_no_selection_text', self.language))
            return

        self.study_page.update_selected_verbs(self.selected_verbs)

        # Navigate to study page
        main_window = self.parent().parent()
        main_window.navigate_to(1)

    def update_verbs(self, verbs: List[Verb]):
        """Update the verbs list."""
        self.verbs = verbs
        self.selected_verbs = []
        self.refresh_verb_list()
        self.verb_count_label.setText(f"{Translations.get('verbs_loaded', self.language)}: {len(self.verbs)} {Translations.get('verbs_verbs', self.language)}")

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
        self.refresh_verb_list()
