names = [1,2,3,4,5,6,7,6,5,43,3]
house = 0

for name in names:
  if name > house:
    house = name
print(house)

# LIST METHODS

numbers = [1,1,6,5,4,4,3,7,8,9,3,2,3,3]
# .insert, .pop, .push, .remove, .replace, .copy, .count, .sort, .reverse
numbers.append('t')
print(numbers)
print(50 in numbers)
numbers.pop()
numbers.sort()
numbers2=numbers.copy()
numbers.reverse()
print(numbers)
print(numbers2)

# REMOVE DUPLICATE LIST

numbers = [1,1,6,5,4,4,3,7,8,9,3,2,3,3]
uniques = []

for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)
      
      