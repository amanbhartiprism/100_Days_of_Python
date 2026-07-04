# =========================================================================
# LESSON 1: LOCAL VS. GLOBAL SCOPE
# =========================================================================

# Global Scope (Defined outside of any functions)
player_health = 10 

def drink_potion():
    # Local Scope (Only exists inside this function)
    potion_strength = 2
    print(f"Inside function (Local player_health): {player_health}") 
    print(f"Inside function (potion_strength): {potion_strength}")

drink_potion()
print(f"Outside function (Global player_health): {player_health}")
# print(potion_strength) # <-- ERROR: This will crash because potion_strength only exists inside the function!


# There is NO Block Scope in Python
# Variables created inside an if/elif/else block or a while/for loop are STILL GLOBAL 
# as long as they are not inside a function.
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0] # This variable is accessible outside this 'if' block!

print(f"Accessed outside 'if' block: {new_enemy}") 


# =========================================================================
# LESSON 2: MODIFYING GLOBAL VARIABLES (The Right Way)
# =========================================================================

enemies_count = 1

def increase_enemies():
    # Bad Practice: using the 'global' keyword can make your code buggy and unpredictable
    # global enemies_count
    # enemies_count += 1
    
    # Best Practice: Use 'return' to modify variables cleanly
    print(f"enemies_count inside function: {enemies_count}")
    return enemies_count + 1

# We reassign the global variable explicitly by capturing the function's output
enemies_count = increase_enemies()
print(f"enemies_count outside function: {enemies_count}")


# =========================================================================
# LESSON 3: GLOBAL CONSTANTS (Python Naming Convention)
# =========================================================================

# If you define a variable that should NEVER change, name it in ALL CAPS.
PI = 3.14159
URL_ENDPOINT = "https://api.github.com"
TWITTER_HANDLE = "@yu_angela"


# =========================================================================
# THE CAPSTONE PROJECT: THE NUMBER GUESSING GAME
# =========================================================================
import random

# Global Constants for Game Balancing
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Compares user guess against the hidden answer. Returns updated remaining turns."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0


def set_difficulty():
    """Captures difficulty level from player and returns matching turn count."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """Executes the complete guessing game logic."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Setup step
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    
    # Core Game Engine Loop
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # Update remaining turn count dynamically
        turns = check_answer(guess, answer, turns)
        
        # Check end-game conditions
        if turns == 0 and guess != answer:
            print("You've run out of guesses, you lose.")
            return  # Exits the function early, cleanly terminating the while loop
        elif guess != answer:
            print("Guess again.\n")

# Start the game block execution
game()