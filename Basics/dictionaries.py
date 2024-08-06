# phone = input("Phone: ")

# digits_mapping = {
#   "1": "One",
#   "2": "Two",
#   "3": "Three",
#   "4": "Four",
#   "5": "Five",
#   "6": "Six",
#   "7": "Seven",
#   "8": "Eight",
#   "9": "Nine",
#   "0": "Xero"

# }

# output = ""

# for characters in phone:
#   output+=digits_mapping.get(characters, "xx") + " "
# print(output)





translator = {
  "day": "adlaw",
  "night": "gabie",
  "afternoon": "udto",

}
while True:
  
  msg = input("> ").lower()
  words = msg.split(' ')
  
  if msg != 'q':
    
    output=""
    for word in words:
      output += translator.get(word,word) + " "
    print(output)
    
  elif msg == 'q':
    break