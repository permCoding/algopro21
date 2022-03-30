import os

workdir = os.getcwd()

list_files = os.listdir(workdir)

filtred = filter(lambda x: x.endswith(('txt','py')), list_files)

# lines = map(lambda x: f"- {x}\n", filtred)
lines = map(lambda x: "- " + x + "\n", filtred)

f = open("list-files.txt", "w", encoding="utf-8")
for line in lines:
    f.write(line+"\n")
f.close()

# with open('list-files.txt', 'w', encoding='utf-8') as f:
#     f.writelines(list(lines))
