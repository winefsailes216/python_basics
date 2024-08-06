
guess_answer = 9
guess_limit = 0


while guess_limit < 3:
  guess = int(input("Guess: "))
  guess_limit +=1
  if guess != guess_answer:
    print("Try again.")
    
  elif guess == guess_answer:
    print("You got it")
    break
  
print("You Failed")