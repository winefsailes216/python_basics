def find_max(numbers):
  maximum = numbers[0]
  for number in numbers:
    if number > maximum:
      maximum = number
  return maximum


# print(find_max([10,2,6,2]))
