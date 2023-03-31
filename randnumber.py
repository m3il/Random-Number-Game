#guess the number
#generate random number, give output to user on what number is between, take input, and tell user if target numner is higher or lower than guessed number 

#imports
import random

#method declarations
def Easy():
    rand = random.randint(0,11)
    print("This game gernerates a random number beween 0 and 10.\nYou have unlimited guesses.\nThe program will tell you if the number is higher or lower than your guess")
    
    guess = input("Press enter to start")
    while guess != rand:
        guess = int(input("A random number beween 0 and 10: "))
        if guess < rand:
            print("The number is higher")
        elif guess > rand:
            print("The number is lower")
    print("Correct! The number is ",rand)
    

def Medium():
    rand = random.randint(0,101)
    print("This game gernerates a random number beween 0 and 100.\nYou have unlimited guesses.\nThe program will tell you if the number is higher or lower than your guess")

    guess = input("Press enter to start")
    while guess != rand:
        guess = int(input("A random number beween 0 and 100: "))
        if guess < rand:
            print("The number is higher")
        elif guess > rand:
            print("The number is lower")
    print("Correct! The number is ",rand)
    
def Hard():
    rand = random.randint(0,101)
    points = 10
    print("This game gernerates a random number beween 0 and 100.\nYou have 10 guesses.\nThe program will tell you if the number is higher or lower than your guess.\nFor every incorrect guess 1 point will be deducted until the total is 0, and you will lose the game")
    guess = input("Press enter to start")
    while guess != rand:
        if points == 0:
            print("You lost, the number is", rand)
        guess = int(input("A random number beween 0 and 100: "))
        if guess < rand:
            print("The number is higher")
            points -= 1
        elif guess > rand:
            print("The number is lower")
            points -= 1
    print("Correct! The number is ",rand)


print("Welcome to Guess the Number.\nPick a level:\n1) Easy\n2) Medium\n3) Hard")
level = input("")
#print(level)
if level == "1":
    Easy()
elif level == "2":
    Medium()
elif level == "3":
    Hard()
else:
    level = input("Please select a level: ")
