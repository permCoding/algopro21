import os

workdir = os.getcwd()
list_files = os.listdir(workdir)

files = filter(lambda x: x.endswith(('pdf','docx','doc','py')), list_files)

lines = list(map(lambda x: x + '\n', files))

with open('list-files.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
