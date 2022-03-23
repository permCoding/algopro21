def get_lines(file_name):
    with open(file_name, encoding="utf-8") as f:
        lines = f.read().split('\n')[1:]
    return lines


def get_objects(lines):
    objects = []
    for line in lines:
        lst = line.split("|")
        objects.append(Student(lst[0], lst[1], lst[2]))
    return objects


class Student:
    def __init__(self, id, full_name, group):
        self.id = int(id)
        sn, fn, on = tuple(full_name.split(" "))
        self.first_name = fn
        self.second_name = sn
        self.other_name = on
        self.group = group
    def __str__(self):
        return f"{self.second_name} {self.first_name}"
