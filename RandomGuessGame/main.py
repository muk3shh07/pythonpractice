import random
UserGuess = int(input("Enter a number between 1 - 6 ::"))

RandomGen = random.randint(1,6)

if UserGuess == RandomGen:
    print("Congratulations!!! your guess is Correct ")
else:
    print("Sorry,Try again.")
    print("\n")
    print(f"The correct guess was {RandomGen}")