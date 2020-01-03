from glob import glob
from os.path import splitext
from os import makedirs, rename

import wordninja


# Extensions to search for.
EXTENSIONS = ('.pdf', '.epub', '.mobi', '.zip')


def create_folder_name(words):
    """ Concatenate words to create the folder name. """
    return ' '.join(words).title()


def create_folder(folder):
    """ Create folder or ignore if it already exists. """
    return makedirs(folder, exist_ok=True)


# Look for all files in the folder and check if they match the expected extensions.
files = [file for file in glob('*') if splitext(file)[-1] in EXTENSIONS]
# Split folders word.
names = [wordninja.split(splitext(file)[0]) for file in files]
# If the exist the same name without the last word, it is probably a supplement, video or something else like  it.
# Then drop the last word.
names = [words[:-1] if words[:-1] in names else words for words in names]
# Create folders and move files.
for file, name in zip(files, names):
    # Create folder.
    folder_name = create_folder_name(name)
    create_folder(folder_name)
    # Move file.
    new_file_name = f'{folder_name}\\{file}'
    print(new_file_name)
    rename(file, new_file_name)
