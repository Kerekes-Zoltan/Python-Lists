def flatten_list(lst1, lst2, lst3):
    return list(lst1 + lst2 + lst3)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]

rez = flatten_list(lst1, lst2, lst3)
print("Flatten list: ", rez)