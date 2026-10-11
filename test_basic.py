"""
Basic test to verify core functionality.
"""

from models.verb import Verb
from utils.csv_importer import CSVImporter
from utils.storage import StorageManager
from utils.themes import get_theme

def test_verb_model():
    """Test verb model."""
    verb = Verb(
        infinitive="be",
        past_simple="was/were",
        past_participle="been",
        spanish_translation="ser/estar",
        row_number=1
    )

    # Test forms
    assert verb.get_forms() == ["be", "was/were", "been", "ser/estar"]
    assert verb.get_form_names() == ["Infinitive", "Past Simple", "Past Participle", "Spanish Translation"]

    # Test validation
    assert verb.is_answer_correct(0, "be") == True
    assert verb.is_answer_correct(0, "BE") == True  # Case insensitive
    assert verb.is_answer_correct(1, "was") == True
    assert verb.is_answer_correct(1, "were") == True  # Compound form
    assert verb.is_answer_correct(3, "ser") == True
    assert verb.is_answer_correct(3, "estar") == True

    print("[OK] Verb model tests passed")

def test_csv_import():
    """Test CSV import."""
    importer = CSVImporter()
    verbs, errors = importer.import_csv("sample_verbs.csv")

    assert len(verbs) == 10, f"Expected 10 verbs, got {len(verbs)}"
    assert len(errors) == 0, f"Expected no errors, got: {errors}"

    # Check first verb
    first_verb = verbs[0]
    assert first_verb.infinitive == "be"
    assert first_verb.past_simple == "was/were"
    assert first_verb.row_number == 1

    print("[OK] CSV import tests passed")

def test_storage():
    """Test storage manager."""
    storage = StorageManager()

    # Test settings
    settings = storage.load_settings()
    assert 'theme' in settings
    assert 'creator_name' in settings

    settings['theme'] = 'dark'
    storage.save_settings(settings)

    loaded = storage.load_settings()
    assert loaded['theme'] == 'dark'

    # Test statistics
    stats = storage.load_statistics()
    assert 'total_questions' in stats
    assert 'sessions' in stats

    stats['total_questions'] = 10
    storage.save_statistics(stats)

    loaded = storage.load_statistics()
    assert loaded['total_questions'] == 10

    print("[OK] Storage tests passed")

def test_themes():
    """Test theme loading."""
    light_theme = get_theme('light')
    dark_theme = get_theme('dark')
    alt_theme = get_theme('alternative')

    assert light_theme.name == 'light'
    assert dark_theme.name == 'dark'
    assert alt_theme.name == 'alternative'

    # Test palette generation
    light_palette = light_theme.get_palette()
    assert light_palette is not None

    # Test stylesheet generation
    light_stylesheet = light_theme.get_stylesheet()
    assert len(light_stylesheet) > 0

    print("[OK] Theme tests passed")

if __name__ == "__main__":
    test_verb_model()
    test_csv_import()
    test_storage()
    test_themes()
    print("\n[SUCCESS] All basic tests passed!")
