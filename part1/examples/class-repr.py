class Matr(object):
    def __init__(self, _tbl):
        self.tbl = _tbl

    def __str__(self):
        result = ['\t'.join(map(str, row)) for row in self.tbl]
        return '\n'.join(result)

t = [[1,2,3], [5,6,7]]
m = Matr(t)
print(m.tbl)
print(m)
