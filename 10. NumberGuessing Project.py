import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
elif difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5
game_over = False
while not game_over:
    guess = int(input("Guess the number: "))
    if guess == computer_number:
        print(f"You guessed the number! in {attempts} attempts")
        game_over = True
    else:
        if guess < computer_number:
            print("Too low!")
            print("guess again!")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            game_over = False
        elif guess > computer_number:
            print("Too high!")
            print("guess again!")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            game_over = False
    if attempts == 0:
        print("You ran out of attempts!")
        game_over = True