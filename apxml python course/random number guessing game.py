import random

random_int = random.randint(0, 100)

while True:
    try:
        user_guess = int(input("Guess a number between 0 and 100: "))
    except ValueError:
        print("Please enter a number")
        continue
    else:
        break

while user_guess != random_int:
    if user_guess < random_int:
        print("Your guess is too low")
        user_guess = int(input("Guess a number between 0 and 100: "))
    if user_guess > random_int:
        print("Your guess is too high")
        user_guess = int(input("Guess a number between 0 and 100: "))

print("You got it!")