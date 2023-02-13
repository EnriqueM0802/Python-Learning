#Program 14: Guessing Game
babyGuess = input("What is the name of the baby in Family Guy")
numberofGuesses = 1

while babyGuess != "Stewie":
    numberofGuesses = numberofGuesses + 1
    if numberofGuesses > 3:
        print("Womp Womp! You lose, you guessed too many times")
        break
    babyGuess = input("Guess again. ")
if numberofGuesses <= 3:
    print("You have guessed it! The name of the baby is Stewie! It took you " + str(numberofGuesses) + " guesses.")