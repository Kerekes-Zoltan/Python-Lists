
def diff_list(lst1, lst2):
    difference = list(set(lst1) - set(lst2))
    return difference

lst1 = [1, 2, 3, 4]
lst2 = [1, 2]

rez = diff_list(lst1, lst2)
print("List1: ", lst1, "\nList2: ", lst2)
print("Difference between two lists: ", rez)