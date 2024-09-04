import os

file_list = []
for dirpath, dirnames, filenames in os.walk('C:\\Users\\areks\\PycharmProjects\\myfastapi\\docs'):
    for filename in filenames:
        if "extra-models" in filename:
            file_list.append(os.path.join(dirpath, filename))