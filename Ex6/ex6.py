def sort_lst(lst):
    return sorted(lst, key=lambda x: x[-1])

data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print("Sorted list: ", sort_lst(data))