def index_list(list, target):
    try:
        return list.index(target)
    except ValueError:
        return -1

list = [1, 2, 3, 4, 5, 6, 7]
target = 1

rez = index_list(list, target)

print(rez)