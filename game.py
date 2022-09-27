import random

top_of_game = input("Enter any number: ")
# input will be type of  string always so we have to convert into integer

if top_of_game.isdigit():
    top_of_game = int(top_of_game)  # we have converting input into integer
    # we have to check wether number is postive or not
    if top_of_game <= 0:
        print("Please enter the Number greate than 0 next time!")
        quit()
else:
    quit()

random_number = random.randint(0, top_of_game)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Make a Guess: ")
    # input will be type of  string always so we have to convert into integer

    if user_guess.isdigit():
        user_guess = int(user_guess)  # we have converting input into integer

    # we have to check wether number is postive or not
    if user_guess <= 0:
        print("Please enter the Number greate than 0 next time!")
        continue
    if user_guess == random_number:
        print("Booom!")
        break

    elif user_guess > random_number:
        print("You are the above the number!")
    else:
        print("You are Below the Number!")

print("You got it in", guess_count, "Guesses! ")
