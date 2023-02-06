def remove_numbers(numbers):
    odd_number = [num for num in numbers if num % 2 != 0]
    return odd_number

numbers = [1, 2, 3, 4, 5]

rez = remove_numbers(numbers)
print("List without even numbers: ", rez)