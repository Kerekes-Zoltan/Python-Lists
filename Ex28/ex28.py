def second_largest(numbers):
  if len(numbers) < 2:
    return None

  first = second = float('-inf')
  for number in numbers:
    if number > first:
      second = first
      first = number
    elif number > second and number != first:
      second = number

  if second == float('-inf'):
    return None

  return second

# Example usage:
numbers = [2, 3, 6, 6, 5]
result = second_largest(numbers)
print("Second largest number is: ", result)