def access_index(elements, target):
    try:
        return elements.index(target)
    except ValueError:
        return -1
    
elements = [1, 2, 3, 4, 5]
target = 3

rez = access_index(elements, target)
print("Index  of the element", target, "in the list: ", rez)