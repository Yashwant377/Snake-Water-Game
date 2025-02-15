user = int(input("Enter 0 for Snake, 1 for Water, 2 for Gun: "))
import random
comp = random.randint(0,2)
if user == 0 and comp == 1:
    print("You win")
elif user == 1 and comp == 2:
    print("You win")
elif user == 2 and comp == 0:
    print("You win")
elif user == comp:
    print("Tie")
else:
    print("You lose")
if comp == 0:
    print("Computer chose Snake")
elif comp == 1:
    print("Computer chose Water")
else:
    print("Computer chose Gun")
if user == 0:
    print("You chose Snake")
elif user == 1:
    print("You chose Water")
else:
    print("You chose Gun")
