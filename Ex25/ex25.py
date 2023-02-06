import random

def random_item(lst):
    return random.choice(lst)

lst = [1, 2, 3, 4, 5]
print("Random item selected from list: ", random_item(lst))