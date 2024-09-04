import os
import re

file_paths_list = []
for dirpath, dirnames, filenames in os.walk('C:\\Users\\areks\\PycharmProjects\\myfastapi\\docs'):
    for filename in filenames:
        if "extra-models" in filename:
            file_paths_list.append(os.path.join(dirpath, filename))

for file_path in file_paths_list:
    with open(file_path, 'rb') as file:
        text = file.read()
    new_text = re.search(
        pattern=rb"####[^\n]+`dict`.*?####[^\n]+`dict`",
        string=text,
        flags=re.MULTILINE | re.DOTALL
    )
    print(file_path, new_text.string)
    with open(file_path, 'wb') as file:
        file.write(text)