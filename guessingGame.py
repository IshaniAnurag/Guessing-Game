import random

randomNumber= random.randint(1,9)


chances=0

while chances<5:
    guess=int(input("Guess a number between 0 and 9: "))
    if(guess==randomNumber):
        print("Congratulations you have won!!")
        break
    elif(guess<randomNumber):
        print("Guess too low!")
    else:
        print("The guess is too high!")

    chances=chances+1

if not chances<5:
    print("You lose!!....The number is: ",randomNumber)
    
      

