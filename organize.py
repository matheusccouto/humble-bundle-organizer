from glob import glob
from os.path import splitext, basename, dirname
from os import makedirs, rename

import wordninja


# Extensions to search for.
EXTENSIONS = ('.pdf', '.epub', '.mobi', '.zip')


def create_name(words):
    """ Concatenate words to create the title name. """
    return ' '.join(words).title()


def create_path(file, name):
    # Get extension
    ext = splitext(file)[-1]
    # Create name.
    file_name = create_name(name)
    # Get path to the file.
    path = dirname(file)
    # If the folder already exist, use it.
    if basename(path) == file_name:
        return f'{path}\\{file_name}{ext}'
    # If the this is the first level of folders, create a new one with the file name.
    elif path == '':
        return f'{file_name}\\{file_name}{ext}'
    # If this is not the  first level of folders and the folder already exists, create a new one with the file name.
    else:
        return f'{path}\\{file_name}\\{file_name}{ext}'


def create_folder(folder):
    """ Create folder or ignore if it already exists. """
    return makedirs(folder, exist_ok=True)


def organize():
    """ Organize files in its folders. """
    # Look for all files in the folder and check if they match the expected extensions.
    files = [file for file in glob('**/*', recursive=True) if splitext(file)[-1] in EXTENSIONS]
    # Split folders word.
    names = [wordninja.split(splitext(basename(file))[0]) for file in files]
    # If the exist the same name without the last word, it is probably a supplement, video or something else like  it.
    # Then drop the last word.
    names = [words[:-1] if words[:-1] in names else words for words in names]
    # Loop through all the files and names
    for file, name in zip(files, names):
        # Get the new path.
        path = create_path(file, name)
        # Create folder.
        create_folder(dirname(path))
        print(path)
        # Move file.
        try:
            rename(file, path)
        except FileExistsError:
            continue


if __name__ == '__main__':
    organize()
