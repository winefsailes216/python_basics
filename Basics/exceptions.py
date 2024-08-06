try:
  age = int(input('Age: '))
  print(age)
except ValueError:
  print("Invalid value, Enter a number.")