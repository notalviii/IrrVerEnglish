# Build Instructions

This document provides instructions for building a standalone executable for IrrVerEnglish v1.0.0.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- All project dependencies installed (see README.md)

## Building with PyInstaller

PyInstaller is a tool that converts Python applications into standalone executables.

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Build the Executable

Navigate to the IrrVerEnglish directory and run:

```bash
pyinstaller --onefile --windowed --name "IrrVerEnglish" --add-data "sample_verbs.csv;." main.py
```

**Explanation of flags:**
- `--onefile`: Creates a single executable file
- `--windowed`: Runs the application without a console window (recommended for GUI apps)
- `--name "IrrVerEnglish"`: Sets the name of the executable

### Step 3: Locate the Executable

After the build completes, the executable will be located in:
```
dist/IrrVerEnglish.exe
```

### Step 4: Test the Executable

Run the executable to verify it works correctly:
```bash
dist/IrrVerEnglish.exe
```

## Advanced Build Options

### Including Additional Files

If you need to include additional files (like the sample CSV), use the `--add-data` flag:

```bash
pyinstaller --onefile --windowed --name "IrrVerEnglish" --add-data "sample_verbs.csv;." main.py
```

Note: On Windows, use semicolon `;` as separator. On Linux/Mac, use colon `:`.

### Creating a Directory Distribution

Instead of a single file, you can create a directory distribution:

```bash
pyinstaller --windowed --name "IrrVerEnglish" main.py
```

This creates a folder with all dependencies, which can be easier to debug.

### Adding an Icon

To add a custom icon to the executable:

```bash
pyinstaller --onefile --windowed --name "IrrVerEnglish" --icon="icon.ico" main.py
```

## Building for Different Platforms

### Windows

The instructions above are for Windows. The executable will be a `.exe` file.

### Linux

On Linux, the command is similar:

```bash
pyinstaller --onefile --windowed --name "IrrVerEnglish" main.py
```

The output will be a binary executable file.

### macOS

On macOS, you can create an app bundle:

```bash
pyinstaller --onefile --windowed --name "IrrVerEnglish" --osx-bundle main.py
```

## Troubleshooting

### Import Errors

If you get import errors when running the executable, try:
1. Build without `--onefile` to see which files are missing
2. Use `--hidden-import` to specify missing modules:
   ```bash
   pyinstaller --onefile --windowed --hidden-import "PyQt6.QtWidgets" main.py
   ```

### Application Won't Start

If the executable fails to start:
1. Try building without `--windowed` to see console output
2. Check that all Python modules are correctly installed
3. Verify the file paths in your code work when packaged

### Large File Size

PyInstaller executables can be large because they include the Python interpreter and all dependencies. This is normal. To reduce size:
- Use UPX compression: `pyinstaller --onefile --windowed --upx-dir=path_to_upx main.py`
- Exclude unused modules with `--exclude-module`

## Alternative: Auto-Py-to-Exe

For a graphical interface to PyInstaller, you can use Auto-Py-to-Exe:

1. Install it:
   ```bash
   pip install auto-py-to-exe
   ```

2. Run it:
   ```bash
   auto-py-to-exe
   ```

3. Use the GUI to configure and build your executable.

## Distribution

Once built, you can distribute the executable:
- The executable is self-contained and doesn't require Python to be installed
- Users can simply run the executable
- No additional installation is needed for the end user

## Notes

- The first time the executable runs, it may be slower than running from source
- All application data (settings, statistics) will be stored in the user's home directory under `.irrverenglish`
- The CSV import feature still requires users to have their own CSV files
