file_name = './csv/groups.csv'

f = open(file_name,mode='r',encoding='utf8')
lines = f.readlines()
f.close()

rows = []
for line in lines[1:]:
    idGr,nameGr,idCur = line.split(',')
    row = (int(idGr),nameGr,int(idCur))
    print(row)
    rows.append(row)

