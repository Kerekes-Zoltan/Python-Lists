def get_frequency(numbers):
  frequency = {}
  for number in numbers:
    if number in frequency:
      frequency[number] += 1
    else:
      frequency[number] = 1

  return frequency

# Example usage:
numbers = [2, 3, 4, 4, 2, 3, 1]
result = get_frequency(numbers)
print("Frequency of elements: ", result)
