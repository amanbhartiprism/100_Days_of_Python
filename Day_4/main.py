import random   #* random module is a different module like in the example mam given with the my module and random before the dot is representing that.
# print("Hello")
# ! Randomisation and Python Lists

# ! Randomisation

# random_integer = random.randint(1,10)
# print (random_integer)

# random_number_0_to_1 = round((random.random() *10),2)
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# ! Generating head or tail

# heads_or_tails_generator = random.randint(0,1)
# if heads_or_tails_generator == 0:
#     print("You've got heads")
# else:
#     print("Yov've got tails")

# ! Lists 
# * Lists are sort of data structure, variables are used for storing a single piece of data but lists are used to store multiple datas generally of same domain. Order here is also importatnt.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
    "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[0])
# print(states_of_america[-2])
# print(len(states_of_america))
# states_of_america[1] = "Pencilvania"         #* changing the components of the list

# states_of_america.append("Angelaland")       #* adding one item into the list
# states_of_america.extend(["Dream land", "Wonder land"])   #* adding multiple item as list into the existing list

# random_state_generator = random.randint(0,49)
# print(f"The random state is: {states_of_america[random_state_generator]}")

# print(states_of_america)

# ! Payment Quiz

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Bad_luck_guy = random.randint(0,4)

# print(f"Today the payment is going to done by: {friends[Bad_luck_guy]}")

# ! by random.choice seq

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# print(random.choice(friends))

# ! Index errors and working with nested lists

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Grapes", "Peaches", "Pears", "Nectarines", "Apples", "Peppers", "Cherries", "Blueberries", "Green Beans"]


# fruits = ["Strawberries", "Grapes", "Peaches", "Pears", "Nectarines", "Apples", "Cherries", "Blueberries"]
# vegetables = ["Spinach", "Kale", "Peppers", "Green Beans"]

# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)
# print(dirty_dozen[1][1])
# print(dirty_dozen[0])              #* here the first bracket is to choose the list and second is to choose the components of the list
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

# ! Rock, Paper and Scissors

#

# ! Gemini code
import random #! Always import at the very top

#! Day 4 Final Project: Rock Paper Scissors
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# #* Store the ASCII art in a list for easy access via index (here we used the same list for both computer and human and gave them to chose from the same different from above)
# game_images = [rock, paper, scissors]

# print("Welcome to the game of Rock, Paper and Scissors")

# # 1. Get User Input
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# # 2. Validation Check (MBA Pro-Tip: Always validate your data!)
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# else:
#     # 3. Show User's Choice
#     print(f"You chose:\n{game_images[user_choice]}")

#     # 4. Generate and Show Computer's Choice
#     computer_choice = random.randint(0, 2)
#     print(f"Computer chose:\n{game_images[computer_choice]}")

#     # 5. Determine the Winner (Simplified Logic)
#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw")

# print("\nThank you for playing!")