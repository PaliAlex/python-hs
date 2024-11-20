import os
import re

def remove_from_directory(dir_name, file_name_part):
    all_files = os.listdir(dir_name)

    some_some = any([file_name_part in string for string in all_files ])

    if not some_some:
        print(f'There is no file with "{file_name_part}" in the name')
        return

    for file_name in all_files:
        some = bool(re.search(file_name_part, file_name))

        if bool(some):
            os.remove(f'{dir_name}/{file_name}')
            print(f"{file_name} - removed!")


remove_from_directory('test_folder', 'some_file')