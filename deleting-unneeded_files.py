#! python3
# A program that walks through a folder tree and searches for
# exceptionally large files or folders (>100M in this case)
# Print these files with their abs path to the screen
import os.path

LARGE_FiLE_SIZE = 1024 * 1024  # 100M, as os.path.getsize(path) returns bytes.


def search_large_file(folder):
    large_files_found = False
    abs_path_folder = os.path.abspath(folder)
    print(f'Searching in {abs_path_folder} for files larger than {LARGE_FiLE_SIZE} ...')
    for foldername, subfolders, filenames in os.walk(abs_path_folder):
        for filename in filenames:
            abs_filename = foldername + os.path.sep + filename
            size = os.path.getsize(abs_filename)
            if size > LARGE_FiLE_SIZE:
                large_files_found = True
                print(f'Find file {abs_filename} larger than {LARGE_FiLE_SIZE}.')
                # os.unlink(abs_filename) # OBS! uncommented if the file really has to be deleted.
    if not large_files_found:
        print(f'No file larger than {LARGE_FiLE_SIZE} found in folder {abs_path_folder}.')
    return large_files_found


folder = 'large_files'
app_folder = '/Applications'
search_large_file(folder)
search_large_file(app_folder)
