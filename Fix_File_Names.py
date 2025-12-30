import os
import re

def replace_spaces_with_underscores_recursive(directory):
    """
    Recursively replaces spaces with underscores in file and folder names
    within the specified directory.
    """
    for root, dirs, files in os.walk(directory):
        # Rename files
        for filename in files:
            if ' ' in filename:
                old_path = os.path.join(root, filename)
                new_filename = filename.replace(' _', '_')
                new_filename = new_filename.replace(' ', '_')
                new_filename = new_filename.replace('1.5_hr', '90_min')
                new_path = os.path.join(root, new_filename)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed file: {old_path} -> {new_path}")
                except OSError as e:
                    print(f"Error renaming file {old_path}: {e}")

        # Rename directories (important to do this after files in the current root
        # to avoid issues with paths changing during file renaming)
        for i in range(len(dirs)):
            dirname = dirs[i]
            if ' ' in dirname:
                old_path = os.path.join(root, dirname)
                new_dirname = dirname.replace(' ', '_')
                new_path = os.path.join(root, new_dirname)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed directory: {old_path} -> {new_path}")
                    # Update the list of directories so os.walk continues correctly
                    dirs[i] = new_dirname
                except OSError as e:
                    print(f"Error renaming directory {old_path}: {e}")


def replace_extension(directory):
    """
    Replaces '.tiff' extension with '.tif' in the specified directory.
    Does not search recursively.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.tiff'):
            old_path = os.path.join(directory, filename)
            new_filename = filename.replace('.tiff', '.tif')
            new_path = os.path.join(directory, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed file: {old_path} -> {new_path}")
            except OSError as e:
                print(f"Error renaming file {old_path}: {e}")

def fix_double_underscores_recursive(directory):
    """
    Recursively replaces spaces with underscores in file and folder names
    within the specified directory.
    """
    for root, dirs, files in os.walk(directory):
        # Rename files
        for filename in files:
            if '__' in filename:
                old_path = os.path.join(root, filename)
                new_filename = filename.replace('__','_')
                new_path = os.path.join(root, new_filename)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed file: {old_path} -> {new_path}")
                except OSError as e:
                    print(f"Error renaming file {old_path}: {e}")

        # Rename directories (important to do this after files in the current root
        # to avoid issues with paths changing during file renaming)
        for i in range(len(dirs)):
            dirname = dirs[i]
            if '__' in dirname:
                old_path = os.path.join(root, dirname)
                new_dirname = dirname.replace('__','_')
                new_path = os.path.join(root, new_dirname)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed directory: {old_path} -> {new_path}")
                    # Update the list of directories so os.walk continues correctly
                    dirs[i] = new_dirname
                except OSError as e:
                    print(f"Error renaming directory {old_path}: {e}")

def fix_naming(directory):
    """
    Recursively replaces spaces with underscores in file and folder names
    within the specified directory.
    """
    for root, dirs, files in os.walk(directory):
        # Rename files
        for filename in files:
            if '_pos_' in filename:
                old_path = os.path.join(root, filename)
                new_filename = filename.replace('_pos_','_pos')
                new_path = os.path.join(root, new_filename)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed file: {old_path} -> {new_path}")
                except OSError as e:
                    print(f"Error renaming file {old_path}: {e}")

        # Rename directories (important to do this after files in the current root
        # to avoid issues with paths changing during file renaming)
        for i in range(len(dirs)):
            dirname = dirs[i]
            if '_pos_' in dirname:
                old_path = os.path.join(root, dirname)
                new_dirname = dirname.replace('_pos_','_pos')
                new_path = os.path.join(root, new_dirname)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed directory: {old_path} -> {new_path}")
                    # Update the list of directories so os.walk continues correctly
                    dirs[i] = new_dirname
                except OSError as e:
                    print(f"Error renaming directory {old_path}: {e}")