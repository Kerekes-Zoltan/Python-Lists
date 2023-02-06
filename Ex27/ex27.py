def small_item(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[1]
    return second_smallest

print("Smallest second number: ", small_item([1, 2, 3, 4, 5]))  #2
print("Second smallest number: ", small_item([1, 1, 2, 3, 4, 5]))   #1