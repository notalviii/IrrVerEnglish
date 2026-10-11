"""
Verb model for IrrVerEnglish.
Represents an irregular verb with its four forms.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Verb:
    """Represents an irregular verb with all four forms."""
    infinitive: str
    past_simple: str
    past_participle: str
    spanish_translation: str
    row_number: int  # Original row number from CSV

    def get_forms(self) -> List[str]:
        """Return all four forms as a list."""
        return [self.infinitive, self.past_simple, self.past_participle, self.spanish_translation]

    def get_form_names(self) -> List[str]:
        """Return the names of the four forms."""
        return ["Infinitive", "Past Simple", "Past Participle", "Spanish Translation"]

    def get_valid_variants(self, form_index: int) -> List[str]:
        """
        Get valid variants for a specific form.
        Handles compound forms like 'was/were' or 'ser/estar'.
        """
        forms = self.get_forms()
        form = forms[form_index]
        return [variant.strip().lower() for variant in form.split('/')]

    def is_answer_correct(self, form_index: int, answer: str) -> bool:
        """
        Check if an answer is correct for a specific form.
        Case-insensitive and handles compound forms.
        """
        valid_variants = self.get_valid_variants(form_index)
        answer_cleaned = answer.strip().lower()
        return answer_cleaned in valid_variants
