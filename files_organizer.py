import os
import shutil
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class FilesOrganizer(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Files Organizer")
        self.setFixedSize(300, 150)

        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        self.organize_button = QPushButton("Organize Files")
        self.organize_button.clicked.connect(self.organize_files)
        layout.addWidget(self.organize_button)

    def organize_files(self) -> None:
        """Prompt for a directory and organize files by extension."""

        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if not directory:
            return

        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if not os.path.isfile(file_path):
                continue

            # Skip this script if it's inside the selected directory
            if os.path.abspath(file_path) == os.path.abspath(__file__):
                continue

            extension = os.path.splitext(file_name)[1].lower()
            folder_name = extension[1:] if extension else "no_extension"
            destination = os.path.join(directory, folder_name)
            os.makedirs(destination, exist_ok=True)

            shutil.move(file_path, os.path.join(destination, file_name))

        QMessageBox.information(self, "Files Organized", "Files have been organized successfully!")


def main() -> None:
    """Run the application."""

    app = QApplication(sys.argv)
    window = FilesOrganizer()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
