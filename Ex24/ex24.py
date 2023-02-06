def append_list(lst1, lst2):
    return list(lst1 + lst2)

lst1 = [1, 2, 3, 4]
lst2 = ['black', 'white', 'red', 'blue']

rez = append_list(lst1, lst2)

print("Original lists:", "\n", lst1, "\n", lst2, "\nAppended List: ", rez)