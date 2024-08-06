
# While true will make the program in an infinite loop until something is typed, in that case it was quit uner elif
while True: 

  name = input("Type in your name: ")

  if len(name) < 3:
    print("Name must be at least 3 characters")
    
  elif len(name) > 20:
    print("Name can only have a maximum of 20 characters")
  
  elif name.lower() == "quit":
    break
  
  else:
    print("Name looks good!")