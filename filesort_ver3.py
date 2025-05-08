import os
import shutil

# Base folder path
BASE_PATH = r"C:/Users/sujit/OneDrive/Documents/practicer/"

# Extension to folder name mapping
FILE_TYPE_MAPPING = {
    ".xlsx": "Excel files",
    ".docx": "Text files",
    ".txt": "Word files",
    ".pptx": "PPT files",
    ".jpg": "Image files",
    ".jpeg": "Image files",
    ".bmp": "Image files"
}

def create_folders(base_path, mapping):
    """Create folders based on file type mapping."""
    for folder in set(mapping.values()):
        folder_path = os.path.join(base_path, folder)
        try:
            os.makedirs(folder_path, exist_ok=True)
        except PermissionError:
            print(f"Permission error: Unable to create folder {folder_path}. Check your permissions.")
        except Exception as e:
            print(f"Unexpected error while creating folder {folder_path}: {e}")

def organize_files(base_path, mapping):
    """Organize files into their respective folders."""
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext.lower()

            if ext in mapping:
                dest_folder = os.path.join(base_path, mapping[ext])
                dest_path = os.path.join(dest_folder, file)

                try:
                    if not os.path.exists(dest_path):
                        shutil.move(file_path, dest_path)
                        print(f"Moved: {file} → {mapping[ext]}")
                except PermissionError:
                    print(f"Permission error: Unable to move file {file}. Check your permissions.")
                except FileNotFoundError:
                    print(f"File not found: {file}. It may have been moved or deleted.")
                except Exception as e:
                    print(f"Unexpected error while moving {file}: {e}")

# Running the code
create_folders(BASE_PATH, FILE_TYPE_MAPPING)
organize_files(BASE_PATH, FILE_TYPE_MAPPING)
