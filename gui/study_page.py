"""
Study page for IrrVerEnglish.
Handles interactive quizzes.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QLineEdit, QFrame, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
from typing import List
import random
from models.verb import Verb
from utils.storage import StorageManager
from utils.translations import Translations
from datetime import datetime


class StudyPage(QWidget):
    """Page for interactive quizzes."""

    def __init__(self, verbs: List[Verb], selected_verbs: List[Verb], storage: StorageManager, language: str = 'en'):
        super().__init__()
        self.verbs = verbs
        self.selected_verbs = selected_verbs
        self.storage = storage
        self.language = language

        self.current_verb = None
        self.prompt_form_index = 0
        self.quiz_verbs = []
        self.current_index = 0
        self.session_results = {
            'correct': 0,
            'incorrect': 0,
            'total': 0
        }

        self.init_ui()

    def update_language(self, language: str):
        """Update language."""
        self.language = language
        # Quiz stays in English as requested
        pass

    def init_ui(self):
        """Initialize the study page UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Title
        title_label = QLabel("Quiz Mode")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        # Info label
        self.info_label = QLabel(f"Select verbs to start a quiz")
        self.info_label.setStyleSheet("font-size: 14px; color: #666;")
        layout.addWidget(self.info_label)

        layout.addSpacing(20)

        # Quiz container
        self.quiz_container = QFrame()
        self.quiz_container.setObjectName("quizContainer")
        self.quiz_container.setStyleSheet("""
            QFrame#quizContainer {
                border: 2px solid #ccc;
                border-radius: 8px;
                padding: 20px;
                background-color: transparent;
            }
        """)
        quiz_layout = QVBoxLayout(self.quiz_container)
        quiz_layout.setSpacing(15)

        # Progress
        self.progress_label = QLabel("")
        self.progress_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        quiz_layout.addWidget(self.progress_label)

        # Prompt form
        self.prompt_label = QLabel("")
        self.prompt_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2196F3;")
        quiz_layout.addWidget(self.prompt_label)

        quiz_layout.addSpacing(10)

        # Answer fields
        self.answer_fields = []
        form_names = ["Infinitive", "Past Simple", "Past Participle", "Spanish Translation"]

        for i in range(4):
            field_layout = QHBoxLayout()
            field_layout.setSpacing(10)

            label = QLabel(form_names[i] + ":")
            label.setStyleSheet("font-size: 14px; font-weight: bold;")
            field_layout.addWidget(label)

            line_edit = QLineEdit()
            line_edit.setPlaceholderText("Enter answer...")
            line_edit.setStyleSheet("font-size: 14px; padding: 8px;")
            field_layout.addWidget(line_edit)

            self.answer_fields.append(line_edit)
            quiz_layout.addLayout(field_layout)

        quiz_layout.addSpacing(10)

        # Check button
        self.check_btn = QPushButton("Check Answers")
        self.check_btn.clicked.connect(self.check_answers)
        self.check_btn.setStyleSheet("font-size: 14px; padding: 10px;")
        quiz_layout.addWidget(self.check_btn)

        # Results
        self.results_label = QLabel("")
        self.results_label.setStyleSheet("font-size: 14px;")
        quiz_layout.addWidget(self.results_label)

        quiz_layout.addSpacing(10)

        # Navigation buttons
        nav_layout = QHBoxLayout()
        nav_layout.setSpacing(10)

        self.next_btn = QPushButton("Next Verb")
        self.next_btn.clicked.connect(self.next_verb)
        self.next_btn.setEnabled(False)
        nav_layout.addWidget(self.next_btn)

        self.repeat_btn = QPushButton("Repeat Quiz")
        self.repeat_btn.clicked.connect(self.repeat_quiz)
        nav_layout.addWidget(self.repeat_btn)

        self.finish_btn = QPushButton("Finish Quiz")
        self.finish_btn.clicked.connect(self.finish_quiz)
        self.finish_btn.setEnabled(False)
        nav_layout.addWidget(self.finish_btn)

        quiz_layout.addLayout(nav_layout)

        self.quiz_container.setVisible(False)
        layout.addWidget(self.quiz_container)

        # Start button
        self.start_btn = QPushButton("Start Quiz")
        self.start_btn.clicked.connect(self.start_quiz)
        self.start_btn.setStyleSheet("font-size: 16px; padding: 12px;")
        layout.addWidget(self.start_btn)

        layout.addStretch()

    def update_verbs(self, verbs: List[Verb]):
        """Update the verbs list."""
        self.verbs = verbs

    def update_selected_verbs(self, selected_verbs: List[Verb]):
        """Update the selected verbs list."""
        self.selected_verbs = selected_verbs
        if selected_verbs:
            self.info_label.setText(f"{len(selected_verbs)} verbs selected")
        else:
            self.info_label.setText("Select verbs to start a quiz")

    def start_quiz(self):
        """Start a new quiz session."""
        if not self.selected_verbs:
            QMessageBox.warning(self, "No Selection", "Please select verbs from the Verbs page first.")
            return

        self.quiz_verbs = self.selected_verbs.copy()
        random.shuffle(self.quiz_verbs)
        self.current_index = 0
        self.session_results = {
            'correct': 0,
            'incorrect': 0,
            'total': 0
        }

        self.quiz_container.setVisible(True)
        self.start_btn.setVisible(False)
        self.show_current_verb()

    def show_current_verb(self):
        """Show the current verb for the quiz."""
        if self.current_index >= len(self.quiz_verbs):
            self.finish_quiz()
            return

        self.current_verb = self.quiz_verbs[self.current_index]

        # Randomly select which form to show as prompt
        self.prompt_form_index = random.randint(0, 3)

        # Update progress
        self.progress_label.setText(f"Question {self.current_index + 1} of {len(self.quiz_verbs)}")

        # Show prompt form
        form_names = self.current_verb.get_form_names()
        forms = self.current_verb.get_forms()

        self.prompt_label.setText(f"{form_names[self.prompt_form_index]}: {forms[self.prompt_form_index]}")

        # Clear and configure answer fields
        for i, field in enumerate(self.answer_fields):
            field.clear()
            field.setEnabled(True)
            field.setStyleSheet("font-size: 14px; padding: 8px;")

            if i == self.prompt_form_index:
                # This is the prompt form, fill it and disable
                field.setText(forms[self.prompt_form_index])
                field.setEnabled(False)
                field.setStyleSheet("font-size: 14px; padding: 8px; background-color: #f0f0f0;")

        self.results_label.setText("")
        self.check_btn.setEnabled(True)
        self.next_btn.setEnabled(False)
        self.finish_btn.setEnabled(False)

    def check_answers(self):
        """Check the user's answers."""
        if not self.current_verb:
            return

        correct_count = 0
        incorrect_count = 0
        results_text = []

        form_names = self.current_verb.get_form_names()
        forms = self.current_verb.get_forms()

        for i, field in enumerate(self.answer_fields):
            if i == self.prompt_form_index:
                continue

            user_answer = field.text().strip()
            is_correct = self.current_verb.is_answer_correct(i, user_answer)

            if is_correct:
                correct_count += 1
                field.setStyleSheet("font-size: 14px; padding: 8px; border: 2px solid #4CAF50;")
                results_text.append(f"✓ {form_names[i]}: Correct")
            else:
                incorrect_count += 1
                field.setStyleSheet("font-size: 14px; padding: 8px; border: 2px solid #f44336;")
                results_text.append(f"✗ {form_names[i]}: Incorrect (expected: {forms[i]})")

        self.session_results['correct'] += correct_count
        self.session_results['incorrect'] += incorrect_count
        self.session_results['total'] += (correct_count + incorrect_count)

        self.results_label.setText("\n".join(results_text))
        self.check_btn.setEnabled(False)
        self.next_btn.setEnabled(True)
        self.finish_btn.setEnabled(True)

    def next_verb(self):
        """Move to the next verb."""
        self.current_index += 1
        self.show_current_verb()

    def repeat_quiz(self):
        """Repeat the current quiz with the same verbs."""
        if not self.quiz_verbs:
            QMessageBox.warning(self, "No Quiz", "No quiz to repeat. Start a new quiz first.")
            return

        if QMessageBox.question(
            self,
            "Repeat Quiz",
            "Do you want to repeat the quiz with the same verbs?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        ) == QMessageBox.StandardButton.Yes:
            self.current_index = 0
            self.session_results = {
                'correct': 0,
                'incorrect': 0,
                'total': 0
            }
            random.shuffle(self.quiz_verbs)
            self.show_current_verb()

    def finish_quiz(self):
        """Finish the quiz and show results."""
        self.quiz_container.setVisible(False)
        self.start_btn.setVisible(True)

        # Calculate accuracy
        total = self.session_results['total']
        if total > 0:
            accuracy = (self.session_results['correct'] / total) * 100
        else:
            accuracy = 0

        # Show results
        result_text = (
            f"Quiz Results:\n\n"
            f"Total Questions: {total}\n"
            f"Correct: {self.session_results['correct']}\n"
            f"Incorrect: {self.session_results['incorrect']}\n"
            f"Accuracy: {accuracy:.1f}%"
        )

        QMessageBox.information(self, "Quiz Complete", result_text)

        # Save statistics
        self.save_session_results(total, self.session_results['correct'], self.session_results['incorrect'], accuracy)

    def save_session_results(self, total: int, correct: int, incorrect: int, accuracy: float):
        """Save the session results to statistics."""
        stats = self.storage.load_statistics()

        stats['total_questions'] += total
        stats['total_correct'] += correct
        stats['total_incorrect'] += incorrect

        session = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total': total,
            'correct': correct,
            'incorrect': incorrect,
            'accuracy': accuracy
        }
        stats['sessions'].append(session)

        self.storage.save_statistics(stats)
