print("This is a weight converter")

while True: 
  try:
    weight = int(input("Enter your weight: "))
    initial = weight
    conversion = input("(L)bs or (K)gs: ")
    
    if conversion.lower() == 'l':
      weight = weight * 0.45
      print(f"Your initial weight is {initial} lbs which is equal to {weight} kgs")

    elif conversion.lower() == 'k':
      weight = weight / 0.45
      print(f"Your initial weight is {initial} kgs  which is equal to {weight} lbs")

    elif conversion.lower() == 'q':
      break
    
    else:
      print("Please enter a valid conversion.")
      
  except ValueError:
    print("Invalid value, Enter a number.")
  
  
  