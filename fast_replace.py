import os

file_paths_list = []
for dirpath, dirnames, filenames in os.walk('C:\\Users\\areks\\PycharmProjects\\myfastapi\\docs'):
    for filename in filenames:
        if "extra-models" in filename:
            file_paths_list.append(os.path.join(dirpath, filename))

for file_path in file_paths_list:
    with open(file_path, 'r') as file:
        text = file.read()
    with open(file_path, 'w') as file:
        file.write(text)