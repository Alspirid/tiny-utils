import os
import re
import shutil

FOLDER_PATH = "/Volumes/G-DRIVE mobile USB/Photos"
FOLDER_PATTERN = r'(\d{4})([-_])(\d{2})\2(\d{2})'


def restructure_folders(input_path):
    pattern = r'(\d{4})([-_])(\d{2})\2(\d{2})'  # Updated pattern

    for item in os.listdir(input_path):
        item_path = os.path.join(input_path, item)
        if os.path.isdir(item_path):
            match = re.match(pattern, item)
            if match:
                year, separator, month, day = match.groups()  # Updated unpacking
                new_structure = os.path.join(input_path, year, month, day)

                # Create new folder structure
                os.makedirs(new_structure, exist_ok=True)

                # Move contents
                for content in os.listdir(item_path):
                    src = os.path.join(item_path, content)
                    dst = os.path.join(new_structure, content)
                    shutil.move(src, dst)

                # Remove old folder
                os.rmdir(item_path)
                print(f"Restructured: {item} -> {new_structure}")
            else:
                print(f"Skipped: {item} (doesn't match expected format)")


# Main execution

# distinct_years = get_distinct_years(FOLDER_PATH)
# print("Distinct years found:", distinct_years)

# Restructure folders
restructure_folders(FOLDER_PATH)
print("Restructuring process completed.")
