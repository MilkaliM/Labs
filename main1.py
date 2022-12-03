from random import randint

nbr1 = randint(1, 6)
nbr2 = randint(1, 6)
print("The sum of dice is ", nbr1, " + ", nbr2, " = ", nbr1 + nbr2, sep="")

if nbr1 + nbr2 == 7 or nbr1 + nbr2 == 11:
    print("You won")
elif nbr1 + nbr2 == 2 or nbr1 + nbr2 == 3 or nbr1 + nbr2 == 12:
    print("You lose")
else:
    print(0)
