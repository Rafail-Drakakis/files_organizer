# Files Organizer

Files Organizer is a simple desktop tool built with Python and PyQt5. It helps tidy up a directory by moving files into folders based on their file extensions. Each file type ends up in its own folder (for example, `jpg` files in a folder named `jpg`). Files without an extension are placed in a folder named `no_extension`.

## Features

- Select a directory through a graphical file dialog.
- Automatically create folders for each file extension.
- Move files into their respective folders.
- Skip files that are not regular files or the script itself.
- Inform the user when the operation is complete.

## Installation

1. Clone the repository.

   ```bash
   git clone <repo-url>
   cd files_organizer
   ```

2. Install the required dependency (PyQt5).

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with Python:

```bash
python files_organizer.py
```

1. Click **Organize Files**.
2. Choose the directory you want to organize.
3. The application will create folders named after each file extension and move the files accordingly. A message box will confirm completion.
