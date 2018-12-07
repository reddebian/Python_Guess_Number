import random

y = int(input("Amount of Numbers: "))
x = random.randint(1, y)

z = int(input("Guess: "))

while (z != x):
  z = int(input("Guess: "))
  if (z > x):
    print("Number is too big!")
  elif (z < x):
    print("Number is too small!")
    
print("Well done, you guessed the number")
input()
