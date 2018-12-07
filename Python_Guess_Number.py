import random

y = int(input("Anzahl der Zahlen: "))
x = random.randint(1, y)

z = int(input("Rate: "))

while (z != x):
  z = int(input("Rate: "))
  if (z > x):
    print("Zahl zu groß!")
  elif (z < x):
    print("Zahl ist zu klein!")
    
print("Super du hast es geschafft!")
input()
