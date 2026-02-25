import random
from hangman_arts import stages, logo
from hangman_words import word_list

lives = 6
print("*****************Welcome to the Hangman game*****************")
print(logo)

chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for letter in range(word_length):
    placeholder += "_"
print(placeholder)

# --- ADD THIS BEFORE THE LOOP ---
correct_letters = []
all_guesses = [] # This is your memory for BOTH right and wrong guesses
game_over = False

while not game_over:
    print(f"*****************************{lives}/6 LIVES LEFT******************************")
    
    # Optional: Show them what they've already tried
    print(f"History: {', '.join(all_guesses)}") 
    
    guess = input("Guess a letter: ").lower()

    # --- THE GATEKEEPER (Change starts here) ---
    if guess in all_guesses:
        print(f"You've already guessed '{guess}'. Try something else!")
        continue # This 'jumps' back to the start and DOES NOT reduce lives
    
    all_guesses.append(guess) # Store the new guess immediately
    # --- THE GATEKEEPER (End of change) ---

    # Your display logic continues below as normal...
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(stages[lives])


