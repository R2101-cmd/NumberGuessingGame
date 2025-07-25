import random
secret=random.randint(0,20)
print("I'm thinking of a number between 1 and 20. Only 6 chances to find the number.")
for guess_f in range(1,7):
  print("Take a guess")
  guess=int(input('>'))
  if guess < secret:
    print("Your guess is too low.")
  elif guess > secret:
    print("Your guess is too high.")
  else:
    break
if guess == secret:
  print("Your guess is correct! You got it in "+str(guess_f)+ " gusses :) ")
else:
  print("Sorry! The number is " +str(secret)+ " please try again later:( " )
