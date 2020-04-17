#! python3
# A program that walks through a folder tree and searches for files with
# a certain file extension, such as .pdf or .jpg. Copy these files from whatever
# location they are in to a new folder.
import os.path
import shutil


# Walk through the entire src folder tree and search all the files with .pdf or .jpg extensions
def selective_copy(src_folder, dst_folder, extentions):
    abs_src_folder = os.path.abspath(src_folder)
    abs_dst_folder = os.path.abspath(dst_folder)
    print(f'Searching in folder {src_folder} all files with extentions {extentions} to folder {dst_folder} ... ')
    for foldername, subfolders, filenames in os.walk(abs_src_folder):
        for filename in filenames:
            stem, suffix = os.path.splitext(filename)
            if suffix in extentions:
                abs_file_path = foldername + os.path.sep + filename
                print(f'Copying file {filename} to folder {dst_folder} ... ')
                shutil.copy(abs_file_path, abs_dst_folder)


src_folder = 'source_folder'
dst_folder = 'target_folder'
extentions = ['.pdf', '.jpg']
selective_copy(src_folder, dst_folder, extentions)
