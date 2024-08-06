numbers = [2,3,4,2,7,8,4,1,1]

# This is a function
def sorting (list, choice):
  if choice == "asc":
    list.sort()
    print(list)
  elif choice == "dsc":
    list.sort()
    list.reverse()
    print(list)
  elif choice == "none":
    print(numbers)
  else:
    print("I don't understand")
#  function end   # 
    
while True: 
  choice = input("Enter choice (asc, dsc, none): ") 
  if choice.lower() != 'q':
    sorting(numbers, choice) #this is how to use function with passing parameters
  elif choice.lower() == 'q':
    break


# Return function for calculations

def square(number):
  return number*number

answer = square(4)
print(square(4))
print(answer)




#REUSABLE FUNCTION
# function def
def translation_function(msg):
  words = msg.split(' ')
  translator = {
    "day": "adlaw",
    "night": "gabie",
    "afternoon": "udto",
  }
  output=""
  for word in words:
    output += translator.get(word,word) + " "
  return output
  
# main program
msg = input("> ").lower()
print(translation_function(msg))
