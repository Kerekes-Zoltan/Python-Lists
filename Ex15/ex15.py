import random

def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers

numbers = [1, 2, 3, 4, 5, 6]

rez = shuffle_list(numbers)

print("Shuffled List: ", rez)