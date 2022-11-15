#Rock, Paper and Scissor Game using Python 

import random

print("Welcome to the Rock, Paper and Scissor Game!")
print("You will be playing against the computer.")

Value = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissor: "))
Computer_Value = random.randint(0,2)

if Value == 0:
    if Computer_Value == 0:
        print("You choose Rock and the computer choose Rock. It's a tie!")
    elif Computer_Value == 1:
        print("You choose Rock and the computer choose Paper. You lose!")
    elif Computer_Value == 2:
        print("You choose Rock and the computer choose Scissor. You win!")
    else:
        print("Enter the valid number.")
elif Value == 1:
    if Computer_Value == 0:
        print("You choose Paper and the computer choose Rock. You win!")
    elif Computer_Value == 1:
        print("You choose Paper and the computer choose Paper. It's a tie!")
    elif Computer_Value == 2:
        print("You choose Paper and the computer choose Scissor. You lose!")
    else:
        print("Enter the valid number.")
elif Value == 2:
    if Computer_Value == 0:
        print("You choose Scissor and the computer choose Rock. You lose!")
    elif Computer_Value == 1:
        print("You choose Scissor and the computer choose Paper. You win!")
    elif Computer_Value == 2:
        print("You choose Scissor and the computer choose Scissor. It's a tie!")
    else:
        print("Enter the valid number.")
else:
    print("Enter the valid number.")