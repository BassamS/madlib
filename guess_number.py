import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0   
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))        
        if guess < random_number:
            print("Sorry, guess again. Too low.")
            # print(random_number)
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
            # print(random_number)
        
    print(f"You are right! You have guessed the number {random_number} correctly!")
guess(10)