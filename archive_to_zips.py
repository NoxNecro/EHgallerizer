import os
import zipfile

def get_image_files(folder_path):
    # List all files in the folder and filter for images
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
    return image_files

def create_zip_archive(folder_path, image_files, max_size_mb=490):
    zip_counter = 1
    zip_files = []
    current_files = []
    current_size = 0

    # Go through the image files and group them based on the max size limit
    for image in image_files:
        image_path = os.path.join(folder_path, image)
        file_size = os.path.getsize(image_path)

        # If adding this file exceeds the size limit, create a new archive
        if current_size + file_size > max_size_mb * 1024 * 1024:
            # Create zip with the current set of files
            zip_file = os.path.join(folder_path, f"archive_{zip_counter}.zip")
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in current_files:
                    zipf.write(file, os.path.basename(file))
                    # Delete the file after adding it to the zip archive
                    os.remove(file)
            zip_files.append(zip_file)
            zip_counter += 1
            current_files = [image_path]
            current_size = file_size
        else:
            current_files.append(image_path)
            current_size += file_size

    # Handle remaining files in the last archive
    if current_files:
        zip_file = os.path.join(folder_path, f"archive_{zip_counter}.zip")
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in current_files:
                zipf.write(file, os.path.basename(file))
                # Delete the file after adding it to the zip archive
                os.remove(file)
        zip_files.append(zip_file)

    return zip_files

def main():
    # Use the current working directory where the script is run
    folder_path = os.getcwd()
    image_files = get_image_files(folder_path)
    if not image_files:
        print("No image files found in the folder.")
        return
    zip_files = create_zip_archive(folder_path, image_files)
    print(f"Created {len(zip_files)} zip archives.")
    return zip_files

# Example usage
main()
