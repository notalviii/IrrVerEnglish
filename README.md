# IrrVerEnglish v1.0.0

## Overview

IrrVerEnglish v1.0.0 is a desktop application designed to help users learn and practise English irregular verbs through interactive quizzes. The application allows you to import custom verb lists from CSV files, select specific verbs to study, and track your progress with detailed statistics. With a modern, intuitive interface and multiple visual themes, IrrVerEnglish provides a flexible and effective learning experience.

## Main Features

- **Interactive Quizzes**: Test your knowledge with randomised questions that show one verb form and ask you to provide the other three.
- **Four Verb Forms**: Study all four forms of each verb: Infinitive, Past Simple, Past Participle, and Spanish Translation.
- **Answer Validation**: Intelligent validation that accepts compound forms (e.g., "was/were", "ser/estar") and is case-insensitive.
- **Random Question Prompts**: Each quiz randomly selects which verb form to display as the prompt.
- **CSV Import**: Import your own custom verb lists from CSV files without requiring an internet connection.
- **Custom Verb Selection**: Choose exactly which verbs to study through individual selection or row range selection.
- **Row-Range Selection**: Select a specific interval of verbs from your CSV file (e.g., rows 10-30).
- **Search and Filtering**: Quickly find verbs in your list using the search functionality.
- **Score Tracking and Statistics**: Track your performance with detailed statistics including accuracy, correct/incorrect answers, and session history.
- **Six Visual Themes**: Choose from Light, Dark, Alternative, Samurai (Japanese-inspired black and white), Sunset (warm colors), and Forest (natural green) themes with gradient backgrounds.
- **Multilingual UI Support**: Interface available in English and Spanish. The quiz mode remains in English for learning purposes.
- **Local Settings and Data Storage**: All preferences and statistics are stored locally on your computer.
- **Creator Information**: Creator name "not_alviii" displayed in the application.

## CSV File Format

IrrVerEnglish uses CSV files to import verb lists. Each verb must be on a separate row with exactly four columns in the following order:

```
Infinitive,Past Simple,Past Participle,Spanish Translation
```

### Example CSV File

```csv
be,was/were,been,ser/estar
go,went,gone,ir
write,wrote,written,escribir
```

### Important Notes

- Each verb occupies one row.
- Headers are not required but can be included (they will be treated as invalid data).
- All four columns must be present and non-empty for a verb to be imported.
- Compound forms should be separated by forward slashes (e.g., "was/were", "ser/estar").
- The file must be UTF-8 encoded.
- The order of rows is preserved and used for row-range selection.

### Adding New Verbs

To add new verbs, simply append them to your CSV file following the format above. For example:

```csv
be,was/were,been,ser/estar
become,became,become,convertirse
begin,began,begun,empezar
break,broke,broken,romper
bring,brought,brought,traer
buy,bought,bought,comprar
choose,chose,chosen,elegir
do,did,done,hacer
go,went,gone,ir
write,wrote,written,escribir
```

## Installation

### Option 1: Using the Executable (No Installation Required)

A pre-built Windows executable (`IrrVerEnglish.exe`) is included in the `dist` folder. Simply:

1. Download or extract the project folder
2. Navigate to the `dist` folder
3. Double-click `IrrVerEnglish.exe` to run

No Python installation or dependencies are required when using the executable.

### Option 2: Running from Source

If you prefer to run from source code or modify the application:

**Prerequisites:**
- Python 3.8 or higher
- pip (Python package manager)

**Installing Dependencies:**

1. Navigate to the IrrVerEnglish directory:
   ```bash
   cd "IrrVerEnglish - not_alviii"
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

The application requires PyQt6 for the graphical interface. The `requirements.txt` file specifies the exact version needed.

## How to Run

### Option 1: Using the Executable (Recommended)

A pre-built Windows executable is included in the `dist` folder. Simply:

1. Navigate to the `dist` folder
2. Double-click `IrrVerEnglish.exe` to run the application

No Python installation is required when using the executable.

### Option 2: Running from Source

To start IrrVerEnglish from source code, run the following command from the project directory:

```bash
python main.py
```

The application window will open, and you can begin using IrrVerEnglish immediately.

## How to Use

### 1. Open IrrVerEnglish

Launch the application by running `python main.py`. The main window will appear with a navigation sidebar on the left and content area on the right.

### 2. Import a CSV File

1. Navigate to the **Verbs** page using the sidebar.
2. Click the **Import CSV File** button.
3. Select your CSV file using the file explorer.
4. The application will import valid verbs and display any errors encountered.
5. The number of imported verbs will be shown.

### 3. Browse the Imported Verbs

After importing, all verbs are displayed in a table on the **Verbs** page showing:
- Row number (from the original CSV)
- Infinitive
- Past Simple
- Past Participle
- Spanish Translation

You can use the search box to filter verbs by any of their forms.

### 4. Select Individual Verbs or a Range of Rows

**Individual Selection:**
- Use the checkbox in the first column to select or deselect individual verbs.
- Click **Select All** to select all verbs.
- Click **Deselect All** to clear your selection.
- Click **Invert Selection** to reverse your current selection.

**Row Range Selection:**
1. Click the **Select by Row Range** button.
2. Enter the start row number and end row number.
3. Click OK to select all verbs in that range.
4. You can combine range selection with individual selection.

The number of selected verbs is displayed in real-time.

### 5. Start a Quiz

1. After selecting verbs, click **Start Quiz with Selected Verbs** on the Verbs page, or navigate to the **Study** page and click **Start Quiz**.
2. The quiz will show one verb form (randomly chosen) and ask you to enter the other three.
3. Type your answers in the provided text fields.
4. Click **Check Answers** to see which are correct or incorrect.
5. Correct answers are highlighted in green, incorrect answers in red with the expected form shown.
6. Click **Next Verb** to continue to the next question.
7. When finished, click **Finish Quiz** to see your session results.

### 6. View Statistics and Previous Sessions

Navigate to the **Statistics** page to see:
- Total questions answered
- Total correct answers
- Total incorrect answers
- Overall accuracy percentage
- A table of all previous sessions with date, questions, correct, incorrect, and accuracy

You can reset all statistics by clicking the **Reset All Statistics** button (requires confirmation).

### 7. Change Interface Settings

Navigate to the **Settings** page to:
- Select your preferred theme (Light, Dark, Alternative, Samurai, Sunset, or Forest)
- Select your preferred language (English or Español)
- View the current version information

Note: The creator name is fixed to "not_alviii" and cannot be changed.

Click **Save Settings** to apply changes. The theme will update immediately, and preferences are saved for future sessions.

## Customization

### Changing the Visual Theme

1. Go to the **Settings** page.
2. Select your preferred theme from the dropdown menu:
   - **Light Theme**: Clean, bright interface with gradient backgrounds.
   - **Dark Theme**: Modern dark interface with blue-purple gradients.
   - **Alternative Theme**: Vibrant purple-blue gradient theme.
   - **Samurai Theme**: Japanese-inspired black and white theme with minimalist design.
   - **Sunset Theme**: Warm orange-red gradient theme inspired by sunset colors.
   - **Forest Theme**: Natural green gradient theme inspired by nature.
3. Click **Save Settings**.

The theme change applies immediately and persists across application restarts.

### Changing the Language

1. Go to the **Settings** page.
2. Select your preferred language from the dropdown menu:
   - **English**: All UI elements in English
   - **Español**: All UI elements in Spanish
3. Click **Save Settings**.

**Important**: The quiz mode (Study page) always displays verb forms in English regardless of the selected language, as this is essential for learning English irregular verbs. The language setting only affects menus, buttons, labels, and messages.

The language preference is saved and persists across application restarts.

### Configuring the Creator Name

The creator name is fixed to "not_alviii" and cannot be changed. This name appears in the **About** section and on the Home page.

### Customizing the CSV Content

Edit your CSV file to add, remove, or modify verbs. Remember:
- Maintain the four-column format: Infinitive, Past Simple, Past Participle, Spanish Translation.
- Use forward slashes for compound forms.
- Save the file with UTF-8 encoding.
- Re-import the file in IrrVerEnglish to see changes.

## Project Structure

```
IrrVerEnglish/
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── sample_verbs.csv            # Example CSV file with sample verbs
├── models/                      # Data models
│   ├── __init__.py
│   └── verb.py                  # Verb data class
├── utils/                       # Utility modules
│   ├── __init__.py
│   ├── csv_importer.py          # CSV file import and validation
│   ├── storage.py               # Local storage for settings and statistics
│   └── themes.py                # Theme definitions and color schemes
└── gui/                         # Graphical user interface
    ├── __init__.py
    ├── main_window.py           # Main application window and navigation
    ├── home_page.py             # Home page with overview
    ├── study_page.py            # Quiz interface
    ├── verbs_page.py            # Verb import and selection
    ├── statistics_page.py       # Statistics display
    ├── settings_page.py         # Settings configuration
    └── about_page.py            # About information
```

## Version Information

Current version: **v1.0.0**

This is the initial release of IrrVerEnglish, providing all core functionality for learning English irregular verbs through interactive quizzes.

## Creator

Creator: not_alviii

The default creator name is "not_alviii". You can change this in the Settings page to personalise your installation.

## Troubleshooting

### CSV Files That Cannot Be Imported

**Problem**: The application shows errors when importing a CSV file.

**Solutions**:
- Ensure the file is UTF-8 encoded.
- Verify each row has exactly four columns separated by commas.
- Check that all four columns contain non-empty values.
- Make sure the file is not corrupted or in binary format.
- Try opening the file in a text editor to verify its contents.

### Invalid or Incomplete CSV Rows

**Problem**: Some verbs are not imported, and error messages are shown.

**Solutions**:
- Review the error messages displayed after import.
- Check that each row has four columns: Infinitive, Past Simple, Past Participle, Spanish Translation.
- Ensure no column is empty or contains only whitespace.
- Verify there are no extra commas within the verb forms (unless part of a compound form with slashes).

### Missing Dependencies

**Problem**: ImportError when running the application.

**Solutions**:
- Ensure Python 3.8 or higher is installed.
- Run `pip install -r requirements.txt` from the project directory.
- Check that PyQt6 is installed correctly: `pip show PyQt6`.
- If using a virtual environment, ensure it is activated before installing dependencies.

### Application Startup Errors

**Problem**: The application fails to start or crashes immediately.

**Solutions**:
- Verify you are running from the correct directory.
- Check that all required files are present in the project structure.
- Ensure Python has read/write permissions for the `.irrverenglish` directory in your home folder.
- Try running with `python main.py` from the command line to see error messages.

### Incorrect File Paths

**Problem**: Cannot find the CSV file when importing.

**Solutions**:
- Use the file explorer dialog to navigate to your CSV file.
- Ensure the file has the `.csv` extension.
- Check that the file is not located in a restricted directory.
- Try moving the CSV file to a simpler location (e.g., Desktop or Documents).

### Common Configuration Problems

**Problem**: Settings or statistics are not saved.

**Solutions**:
- Ensure the application has write permissions for your home directory.
- Check that the `.irrverenglish` folder exists in your home directory.
- Verify that `settings.json` and `statistics.json` files are not corrupted.
- Try resetting statistics from the Statistics page if data appears corrupted.

**Problem**: Theme does not change after selection.

**Solutions**:
- Click **Save Settings** after selecting a theme.
- Restart the application if the theme does not update immediately.
- Check that the theme name in settings.json is valid (light, dark, or alternative).

### Performance Issues

**Problem**: Application is slow with large verb lists.

**Solutions**:
- Select a smaller subset of verbs for quizzes.
- Use the search filter to quickly find specific verbs.
- Consider splitting large CSV files into smaller, themed collections.

### Windows Security Warnings

**Problem**: Windows Defender SmartScreen or Intelligent App Control blocks the executable.

**Explanation**: The executable is not digitally signed, which may trigger Windows security warnings. This is normal for self-built applications and does not indicate malware.

**Solutions**:
1. **Windows Defender SmartScreen**:
   - When you run the executable, you may see a "Windows protected your PC" warning
   - Click "More info"
   - Click "Run anyway" to proceed
   - This warning will not appear again after the first run

2. **Windows Intelligent App Control**:
   - If Intelligent App Control is enabled on your system, it may block unsigned applications
   - To allow the application, you may need to:
     - Add an exception in Windows Security settings
     - Disable Intelligent App Control temporarily or permanently
     - Run the application from source code instead (python main.py)

   **To disable Intelligent App Control**:
   - Open Windows Security
   - Go to "App & browser control"
   - Click on "Reputation-based protection settings"
   - Turn off "Check apps and files" or "SmartScreen for Microsoft Edge"
   - Note: Disabling these features reduces your system's security protection

3. **Verify Safety**:
   - The executable is built from the source code in this repository
   - All code is visible and can be reviewed
   - No network connections are made by the application
   - All data is stored locally on your computer

4. **Alternative**: Run from Source
   - If you prefer to avoid executable security warnings, run the application from source:
     ```bash
     python main.py
     ```
   - This requires Python and dependencies to be installed (see Installation section)

## Building an Executable

A pre-built Windows executable (`IrrVerEnglish.exe`) is already included in the `dist` folder and ready to use.

If you need to rebuild the executable (for example, after modifying the source code), you can use PyInstaller:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --name "IrrVerEnglish" --add-data "sample_verbs.csv;." main.py
   ```

   **Note**: On Windows, use semicolon `;` as the separator. On Linux/Mac, use colon `:`.

3. The executable will be created in the `dist` directory.

For more advanced build options, refer to the PyInstaller documentation or see `BUILD.md` for detailed instructions.

## Credits

**Created by**: not_alviii 🧸 and Devin

## License

IrrVerEnglish v1.0.0 - Desktop application for learning and practising English irregular verbs.

## Support

For issues, questions, or suggestions, please refer to the project documentation or contact the creator.
