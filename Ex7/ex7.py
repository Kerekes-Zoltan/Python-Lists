def remove_duplicates(dublicate):
    return list(set(dublicate))

data = [1, 2, 3, 4, 5, 1, 2, 2, 5, 5, 4, 3]

print("List without dublicates: ", remove_duplicates(data))