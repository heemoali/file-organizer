import os
import shutil

# Folders categorized by file type
FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".dmg", ".apk"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".json"],
}


def get_folder_for_extension(extension):
    # Return the appropriate folder name based on the file extension
    for folder, extensions in FOLDERS.items():
        if extension.lower() in extensions:
            return folder
    return "Others"


def organize_folder(path):
    # Organize files inside the given folder
    if not os.path.exists(path):
        print(f"Error: path not found: {path}")
        return

    moved_count = 0

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith("."):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)
        if not extension:
            continue

        # Determine the target folder
        target_folder = get_folder_for_extension(extension)
        target_path = os.path.join(path, target_folder)

        # Create the folder if it does not exist
        os.makedirs(target_path, exist_ok=True)

        # Move the file
        try:
            shutil.move(file_path, os.path.join(target_path, filename))
            print(f"Moved: {filename} -> {target_folder}/")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {filename}: {e}")

    print(f"\nDone. {moved_count} file(s) moved successfully.")


if __name__ == "__main__":
    print("File Organizer")
    print("-" * 30)
    folder_path = input("Enter folder path (or press Enter for Downloads): ").strip()

    if not folder_path:
        folder_path = os.path.join(os.path.expanduser("~"), "Downloads")

    print(f"\nOrganizing: {folder_path}\n")
    organize_folder(folder_path)