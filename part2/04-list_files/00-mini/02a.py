import os

workdir = "."

list_files = os.listdir(workdir)

lines = [x+'\n' for x in list_files if x.endswith(("txt"))]

with open('list-files.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
