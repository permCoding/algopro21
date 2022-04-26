
def get_lines(file_name):
    with open(file_name,mode='r',encoding='utf8') as f:
        return f.readlines()


def get_rows(lines):
    rows = []
    for line in lines[1:]:
        idGr,nameGr,idCur = line.split(',')
        row = (int(idGr),nameGr,int(idCur))
        rows.append(row)
    return rows


def main():
    lines = get_lines('./csv/groups.csv')
    rows = get_rows(lines)
    for row in rows:
        print(row)


if __name__ == "__main__":
	main()
