import random
randomnumber=random.randint(1,100)
userGuess=None
guesses=0
while(userGuess!=randomnumber):
    userGuess=int(input("Enter your guess: "))
    guesses+=1
    if(userGuess==randomnumber):
        print("You guessed it right!")
    else:
        if(userGuess>randomnumber):
            print("You guessed it wrong Enter a smaller number")
        else:
            print("You guessed it wrong Enter a larger number")
print(f"You guessed the number in {guesses} guesses")            
