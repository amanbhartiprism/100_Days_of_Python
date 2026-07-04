# Save this file exactly as main.py in the same folder as the other files
import random
from art import logo, vs
from game_data import data

def get_random_account():
    """Fetches a random dictionary record from the data array."""
    return random.choice(data)


def format_data(account):
    """Parses a specific account dictionary into a scannable console description string."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Performs the numerical validation checks based on user input selection."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    print(logo)
    score = 0
    game_should_continue = True
    
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Loop safety guard check to eliminate duplicates
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print("\n" * 20)
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b
            account_b = get_random_account()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Core initialization trigger
play_game()