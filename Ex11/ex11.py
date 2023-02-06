def check_common(x, y):
    return bool(set(x) & set(y))

list1 = [1]
list2 = [1, 2, 3, 4]
print(check_common(list1, list2))


list1 = []
list2 = [1, 2, 3]
print(check_common(list1, list2))


