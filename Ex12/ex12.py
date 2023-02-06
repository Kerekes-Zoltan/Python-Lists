def remove_elements(lst):
    return [x for i, x in enumerate(lst) if i not in [0, 4, 5]]

colors = ["Red", "Green", "Yellow", "Blue", "Pink", "Purple"]
new_list = remove_elements(colors)
print(new_list) # ['Green', 'Yellow', 'Blue']