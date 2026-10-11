# IrrVerEnglish v1.0.0 - Architecture Overview

## Technology Stack

IrrVerEnglish is built with:
- **Python 3.8+**: Core programming language
- **PyQt6**: GUI framework for the desktop application
- **Standard Library**: csv, json, pathlib, dataclasses, random, datetime

## Architecture

The application follows a Model-View-Controller (MVC) inspired architecture with clear separation of concerns:

### 1. Models Layer (`models/`)

**Purpose**: Data structures and business logic

- **verb.py**: Contains the `Verb` dataclass that represents an irregular verb with all four forms
  - Stores: infinitive, past_simple, past_participle, spanish_translation, row_number
  - Provides validation logic for answers
  - Handles compound forms (e.g., "was/were", "ser/estar")
  - Case-insensitive answer checking

### 2. Utilities Layer (`utils/`)

**Purpose**: Reusable utility functions and services

- **csv_importer.py**: Handles CSV file import and validation
  - Reads CSV files with UTF-8 encoding
  - Validates row structure (exactly 4 columns)
  - Detects and reports errors
  - Returns list of Verb objects

- **storage.py**: Manages local data persistence
  - Stores settings in `~/.irrverenglish/settings.json`
  - Stores statistics in `~/.irrverenglish/statistics.json`
  - Handles JSON serialization/deserialization
  - Provides default values for missing data

- **themes.py**: Defines visual themes
  - LightTheme: Clean, bright interface
  - DarkTheme: Modern dark interface
  - AlternativeTheme: Blue-green color scheme
  - Each theme provides palette and stylesheet

### 3. GUI Layer (`gui/`)

**Purpose**: User interface components

- **main_window.py**: Main application window
  - Navigation sidebar with page selection
  - Content area with stacked widget
  - Theme application
  - Coordinates between all pages

- **home_page.py**: Dashboard/overview page
  - Shows application status
  - Displays loaded verb count
  - Quick action buttons
  - Creator information

- **study_page.py**: Quiz interface
  - Displays current verb question
  - Accepts user answers
  - Validates answers
  - Shows results (correct/incorrect)
  - Tracks session progress
  - Saves session statistics

- **verbs_page.py**: Verb management
  - CSV file import
  - Verb table display
  - Individual verb selection (checkboxes)
  - Bulk selection (Select All, Deselect All, Invert)
  - Row range selection
  - Search/filter functionality
  - Integration with study page

- **statistics_page.py**: Statistics display
  - Overall performance metrics
  - Session history table
  - Reset statistics functionality

- **settings_page.py**: Configuration
  - Theme selection
  - Creator name configuration
  - Version information
  - Settings persistence

- **about_page.py**: Application information
  - Application name and version
  - Description
  - Creator name
  - Release information

## Data Flow

### CSV Import Flow
1. User selects CSV file via file dialog
2. CSVImporter reads and validates the file
3. Valid verbs are converted to Verb objects
4. Verbs are stored in main_window.verbs list
5. All pages are updated with new verb list

### Quiz Flow
1. User selects verbs in VerbsPage
2. Selected verbs are passed to StudyPage
3. StudyPage shuffles selected verbs
4. For each verb:
   - Random form is chosen as prompt
   - User enters other three forms
   - Answers are validated
   - Results are shown
5. Session results are saved to statistics

### Settings Flow
1. User changes settings in SettingsPage
2. Settings are saved to JSON file
3. Main window is notified
4. Theme is applied immediately
5. All pages refresh with new settings

### Statistics Flow
1. Quiz session completes
2. Session results are calculated
3. Results are appended to statistics
4. Statistics are saved to JSON file
5. StatisticsPage loads and displays data

## Key Design Decisions

### PyQt6 Choice
- Modern, actively maintained GUI framework
- Cross-platform compatibility
- Rich widget set
- Professional appearance
- Good documentation

### Local Storage
- No external dependencies (databases, cloud services)
- Simple JSON files for easy inspection
- User data stays on user's computer
- Privacy-focused approach

### CSV-Based Verb Lists
- User control over content
- Easy to edit with any text editor
- Portable format
- No hardcoded verb lists
- Supports custom verb collections

### Theme System
- Palette-based theming
- Stylesheet-based customization
- Easy to add new themes
- Persistent theme preference

### Answer Validation
- Compound form support (slash-separated)
- Case-insensitive comparison
- Whitespace trimming
- Flexible validation without strict rules

## File Structure

```
IrrVerEnglish/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── README.md                  # User documentation
├── BUILD.md                   # Build instructions
├── ARCHITECTURE.md            # This file
├── sample_verbs.csv          # Example CSV file
├── test_basic.py             # Basic functionality tests
├── models/                   # Data models
│   ├── __init__.py
│   └── verb.py
├── utils/                    # Utilities
│   ├── __init__.py
│   ├── csv_importer.py
│   ├── storage.py
│   └── themes.py
└── gui/                      # User interface
    ├── __init__.py
    ├── main_window.py
    ├── home_page.py
    ├── study_page.py
    ├── verbs_page.py
    ├── statistics_page.py
    ├── settings_page.py
    └── about_page.py
```

## Extensibility

The architecture supports easy extension:

### Adding New Themes
1. Create new class inheriting from Theme in `themes.py`
2. Implement `get_palette()` and `get_stylesheet()`
3. Add to `get_theme()` function
4. Update SettingsPage dropdown

### Adding New Statistics
1. Add field to default_stats in `storage.py`
2. Update StatisticsPage to display new metric
3. Update StudyPage to calculate and save new metric

### Adding New Quiz Modes
1. Extend StudyPage with new mode
2. Add UI controls for mode selection
3. Implement mode-specific logic
4. Update statistics tracking if needed

## Performance Considerations

- Verb lists are loaded once per import
- Quiz uses in-memory shuffling (no repeated I/O)
- Statistics are loaded on-demand
- Theme changes are applied immediately without restart
- CSV import is synchronous (acceptable for typical file sizes)

## Security Considerations

- No network connections required
- All data is local
- No external code execution
- CSV parsing is safe (no code execution)
- Settings and stats stored in user home directory
- No secrets or credentials stored

## Testing

Basic tests are provided in `test_basic.py`:
- Verb model validation
- CSV import functionality
- Storage operations
- Theme loading

Run tests with:
```bash
python test_basic.py
```

## Future Enhancements

Potential areas for expansion:
- Audio pronunciation
- More quiz modes (multiple choice, typing)
- Verb difficulty levels
- Spaced repetition algorithm
- Export/import of statistics
- More themes
- Verb conjugation practice
- Progress graphs/charts
