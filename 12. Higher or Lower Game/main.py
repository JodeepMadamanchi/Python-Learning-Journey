from art import logo
from art import vs
from game_data import data
print(logo)
import random
account_a = random.choice(data)
account_b = random.choice(data)
score = 0
game_over = True
while game_over:
    while account_a == account_b:
        account_b = random.choice(data)
    account_name_a = account_a["name"]
    account_description_a = account_a["description"]
    account_country_a = account_a["country"]
    print(f'Compare A: {account_name_a}, a {account_description_a} from {account_country_a}')
    account_name_b = account_b["name"]
    account_description_b = account_b["description"]
    account_country_b = account_b["country"]
    print(vs)
    print(f'With B: {account_name_b}, a {account_description_b} from {account_country_b}')
    guess = input("Who has more followers ? Type 'A' or 'B': ").upper()
    if account_a["follower_count"] > account_b["follower_count"] and guess == "A":
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_a
        account_b = random.choice(data)
        game_over = True
    elif account_a["follower_count"] > account_b["follower_count"] and guess == "B":
        print(f"Sorry you are wrong your final score is {score}")
        game_over = False
    elif account_a["follower_count"] < account_b["follower_count"] and guess == "A":
        print(f"Sorry you are wrong your final score is {score}")
        game_over = False
    elif account_a["follower_count"] < account_b["follower_count"] and guess == "B":
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_b
        account_b = random.choice(data)
        game_over = True
    else:
        print("You have typed invalid input , please try again with 'A' or 'B'")
        game_over = True