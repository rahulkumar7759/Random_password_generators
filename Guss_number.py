
import random
number= random.randint(1,10)
print("You will have three chances to guess the correct number!")
for i in range(0,3):
  a= int(input("Guess the Number: "))
  if a==number:
    print("Hurray!")
    print(f"you guessed the number right it's {number}")
    break
if a != number:
  print(f"Your guess is incorrect. The correct number is {number}.")
