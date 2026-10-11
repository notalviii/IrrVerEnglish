"""
CSV importer for IrrVerEnglish.
Handles importing verbs from CSV files.
"""

import csv
from typing import List, Tuple
from models.verb import Verb


class CSVImporter:
    """Handles CSV file import and validation."""

    @staticmethod
    def import_csv(file_path: str) -> Tuple[List[Verb], List[str]]:
        """
        Import verbs from a CSV file.

        Args:
            file_path: Path to the CSV file

        Returns:
            Tuple of (list of Verb objects, list of error messages)
        """
        verbs = []
        errors = []

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)

                if not rows:
                    errors.append("File is empty.")
                    return verbs, errors

                for row_num, row in enumerate(rows, start=1):
                    # Skip empty rows
                    if not row or all(cell.strip() == '' for cell in row):
                        continue

                    # Validate row has exactly 4 columns
                    if len(row) != 4:
                        errors.append(f"Row {row_num}: Invalid format (expected 4 columns, got {len(row)})")
                        continue

                    # Validate all columns are non-empty
                    if any(cell.strip() == '' for cell in row):
                        errors.append(f"Row {row_num}: Incomplete data (all 4 columns required)")
                        continue

                    # Create verb object
                    verb = Verb(
                        infinitive=row[0].strip(),
                        past_simple=row[1].strip(),
                        past_participle=row[2].strip(),
                        spanish_translation=row[3].strip(),
                        row_number=row_num
                    )
                    verbs.append(verb)

            if not verbs:
                errors.append("No valid verbs found in file.")

        except UnicodeDecodeError:
            errors.append("File encoding error. Please ensure the file is UTF-8 encoded.")
        except Exception as e:
            errors.append(f"Error reading file: {str(e)}")

        return verbs, errors
