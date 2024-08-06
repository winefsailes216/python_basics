is_started = False

while True:
  try:
    command = input("> ").lower()

    if command == "quit":
      break
      
    elif command == "start":
      if not is_started:
        print("Car started")
        is_started = True
      else:
        print("Engine is running")

    elif command == "stop":
      if is_started:
        print("Car stopped")
        is_started = False
      else:
        print("Engine is not running.")
            
    elif command == "help":
      print("""
          start = car started
          stop  = car stoped
          help  = for options
          quit  = to exit the App      
          
          """)
      
    else:
      print("Invalid command.")
    
  except ValueError:
    print("Pease, Enter a valid command")