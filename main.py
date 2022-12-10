#DESCRIPTION
#Dice-Game: A game where as an input user will give a static number between (1-6) and then roll dice which randomly generate some value between(1-6)



#CODE:
import random

print("Welcome to DICE GAME!")

i = ""
scr = 0  # Score
count = 0

while i != "n":
    x = int(input("Enter number from (1-6): "))
    y = random.randint(1, 6)

    if x not in range(1, 6 + 1):
        print("Number must be between 1 to 6!")
    else:
        print(f"({x}, {y})")
        if x == y:
            scr += 1

    if count >= 5:
        i = str(input("Do you want to continue? (Y/n): "))
    count += 1

print("Game Over!")
print("Your Score:", scr)
