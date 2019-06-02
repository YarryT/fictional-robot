import random

random_number = random.randint(1,100)
keep_asking = True
    

while keep_asking:
    user_guess = input("What is your guess?")
    if str.isdigit(user_guess) == False:
        print("You must enter an integer! Try Again!")
    elif int(user_guess) > random_number:
        print("Your guess was too high!")
    elif int(user_guess) == random_number:
        print("Congrats, you guessed the number! Ok bai!")
        break
    elif int(user_guess) < random_number:
        print("Your guess was too low!")
