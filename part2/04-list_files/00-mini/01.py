import os

workdir = os.getcwd()

list_files = os.listdir(workdir)

files = filter(lambda x: x.endswith(('pdf','docx','doc','py')), list_files)

text = '\n'.join(files)

f = open(file='list-files.txt', mode='w', encoding='utf-8')
f.write(text)
f.close()