
import random

def rollTheDice():
    computerInput = random.randint(1,6)
    userInput = int(input("Please enter a number from 1 to 6: "))

    while userInput >6 or userInput <0:
        userInput = int(input("Please enter a number from 1 to 6: "))
    
    print ("computer chose: ", computerInput)
    
    if userInput > computerInput:
        print('you win')
    elif userInput == computerInput:
        print('try again')
        rollTheDice()
    else:
        print('you loose')

rollTheDice()



