import os

workdir = os.getcwd()

list_files = os.listdir(workdir)

full_path_files = list(map(lambda file: os.path.abspath(file) , list_files))

# for file in full_path_files:
#     print(os.path.abspath(file))

# ===================

# может пригодиться далее на лабраб
# когда файлы будут из разных папок

# for file in full_path_files:
#     print(os.path.dirname(file))

set_dirs = set((os.path.dirname(file) for file in full_path_files))
for i, x in enumerate(set_dirs):
    print(i+1, x)
