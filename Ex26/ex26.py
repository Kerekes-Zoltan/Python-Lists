def is_circular(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1 == lst2:
            return True
        lst2 = lst2[1:] + [lst2[0]]
        
    return False

print("Is Circular? ", is_circular([1, 2, 3, 4], [3, 4, 1, 2])) #True
print("Is Circular? ", is_circular([1, 2, 3, 4], [2, 3, 4, 1])) #True
print("Is Circular? ", is_circular([1, 2, 3, 4], [3, 4, 1, 2, 5]))  #False