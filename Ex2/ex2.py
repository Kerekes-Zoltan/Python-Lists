def mult_list(lst):
    rez = 1
    for item in lst:
        rez *= item
    return rez

data = [1, 2, 3, 4, 5]
print("All numbers multiply in list: ", mult_list(data))