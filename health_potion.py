import random

health = random.randint(1,100)
print("Your health is: " + str(health))

difficulty = int(input("Please enter a difficulty level from 1 to 3:"))

potion = int(random.randint(25,50) / difficulty)
print("Potion heals you by: " + str(potion))


health = health + potion
print("Your health is: " + str(health))


if health < 50:
    print("You died!")
else:
    print("You're alive and well!")
