from random import randint

def r():
    nbr1 = randint(1, 6)
    nbr2 = randint(1, 6)
    print("The sum of dice is ", nbr1, " + ", nbr2, " = ", nbr1 + nbr2, sep="")
    return nbr1 + nbr2

def f1(goal):
    print("Now your goal number is ", goal, sep="")
    n = r()
    while(n != goal):
        if n == 7:
            print("You lose")
            return
        n = r()
    print("You won")

nbr = r()
if nbr == 7 or nbr == 11:
    print("You won")
elif nbr == 2 or nbr == 3 or nbr == 12:
    print("You lose")
else:
    f1(nbr)
