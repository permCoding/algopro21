import os

workdir = os.getcwd()
list_files = os.listdir(workdir)
files = filter(lambda x: x.endswith(('pdf','docx','doc')), list_files)

text = '\n'.join(files)

f = open('list-files.txt', 'w', encoding='utf-8')
f.write(text)
f.close()