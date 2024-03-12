import os

def delete_jpg_files():
    # Get the current directory
    current_directory = os.getcwd()

    # Get a list of all files in the current directory
    files = os.listdir(current_directory)

    # Iterate through all files
    for file in files:
        # Check if the file is a JPG file
        if file.lower().endswith('.jpg'):
            try:
                # Attempt to delete the file
                os.remove(os.path.join(current_directory, file))
                print(f"Deleted: {file}")
            except Exception as e:
                # Print an error message if the file could not be deleted
                print(f"Error deleting {file}: {e}")

# Call the function to delete JPG files
delete_jpg_files()