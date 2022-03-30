import os

workdir = os.getcwd()

list_files = os.listdir(workdir)

# print(list_files)
# filtred = filter(lambda x: x.endswith(('pdf','txt')), list_files)

checked = ['txt', 'pdf']
filtred = filter(lambda x: x.split('.')[-1] in checked, list_files)
# print(filtred)
# print(list(filtred))

# for item in filtred:
#     print(item)

lines = '\n'.join(filtred)

print(lines)

f = open(file='list-files.txt', mode='w', encoding='utf-8')
f.write(lines)
f.close()
