# print("Hi")
# ! Control Flow with if / else and Conditional Operators
 
# * if condition:
# *    do this
# * else:
# *    do this

# print("Welcome to the rollercoaster !")
# height = int(input("What is your height in cm?\n"))

# if  height > 120:  #*use the comparison operators to mess with this
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride")
# # * '=' if there is one equal sign it is for assignment. '==' but two equal sign is for checking equality

# ! Modulo Operator - gives the remainder 

# print(10 % 3)
# * Checking the number is even or not
# number = int(input("Enter a number to check if it is even or odd\n"))
# if  number % 2 == 0:
#     print("Hey, it is an even number")
# else:
#     print("Hey, it is an odd number")

# ! Nested if statement        use of elif

# print("Welcome to the rollercoaster !")
# height = int(input("What is your height in cm?\n"))

# if  height > 120:  #*use the comparison operators to mess with this
#     print("You can ride the rollercoaster")
#     age = int(input("But first tell me what is your age\n"))
#     if  age < 12:                               # age <= 12
#         print("Hey, it will we $5")             
#     elif  age > 18:
#         print("Hey, it will we $12")            # age <= 18 you can use this too
#     else:
#         print("Hey, it will we $7")
# else:
#     print("Sorry you have to grow taller before you can ride")

# ! Multiple if in succession

# print("Welcome to the rollercoaster !")
# height = int(input("What is your height in cm?\n"))
# bill = 0
# if  height > 120:  #*use the comparison operators to mess with this
#     print("You can ride the rollercoaster")
#     age = int(input("But first tell me what is your age\n"))
#     if  age <= 12:                               # now adding a charge for photos is independent of age or anything so it needs a multiple if statement
#         bill = 5
#         print("Child ticket would be $5")             
#     elif  age <= 18:
#         bill = 7
#         print("Youth ticket would be $7")            
#     else:
#         bill = 12
#         print("Adult ticket would be $12")
    
#     wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
#     if  wants_photo == "y":
#         bill += 3

#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry you have to grow taller before you can ride")

# ! Pizza Deliveries

# //print("Welcome to the Python Pizza Deliveries")
# //size = input("What size pizza do you want? S for $15, M for $20, L for $25. Please type S,M or L:\n")
# //  size == "S":
# //    bill = 15
# //    print("Small size pizza price would be $15")
# //    wants_pepperoni = input("Do you want pepperoni on your pizza? $1 for pepperoni on small pizzas. Please type Y of N:\n")
# //    if  wants_pepperoni == "Y":
# //      bill += 1

# //elif  size == "M":
# //    bill = 20
# //    print("Medium size pizza price would be $20")
# //    wants_pepperoni = input("Do you want pepperoni on your pizza? $1 for pepporoni on medium pizzas. Please type Y of N:\n")
# //    if  wants_pepperoni == "Y":
# //      bill += 1

# //else:
# //    bill = 25
# //print("Large size pizza price would be $25")
# //    wants_pepperoni = input("Do you want pepperoni on your pizza? $2 for pepporoni on large pizzas. Please type Y of N:\n")
# //    if  wants_pepperoni == "Y":
# //      bill += 2

# //wants_cheese = input("Do you want extra cheese on your pizza? $1 for extra cheese. Please type Y of N:\n")
# //if  wants_cheese == "Y":
# //    bill += 1
# //print(f"Your final bill is: {bill}")

#! Pizza Order Simplification
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# # 1. Set the Base Price (Mutually Exclusive)
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25

# # 2. Add Pepperoni (Independent check)
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# # 3. Add Extra Cheese (Independent check)
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# ! Logical Operators
# print("Welcome to the rollercoaster !")
# height = int(input("What is your height in cm?\n"))
# bill = 0
# if  height > 120:  #*use the comparison operators to mess with this
#     print("You can ride the rollercoaster")
#     age = int(input("But first tell me what is your age\n"))
#     if  age <= 12:                               #* now adding a charge for photos is independent of age or anything so it needs a multiple if statement
#         bill = 5
#         print("Child ticket would be $5")             
#     elif  age <= 18:
#         bill = 7
#         print("Youth ticket would be $7")
#     elif age >= 45 and age <= 55:            #*  45 <= age >= 55
#         print("Everything is going to be okay . Have a free ride on us.")            
#     else:
#         bill = 12
#         print("Adult ticket would be $12")
    
#     wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
#     if  wants_photo == "y":
#         bill += 3

#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry you have to grow taller before you can ride")

# ! PROJECT TREASURE ISLAND  use .lower() while inputing so it even works even thouh user type something else

# print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?")

# Cross_road = input("Type left or right\n").lower()

# if Cross_road == "left":
#     print("You've come to a lake. There is an island in the middle of the lake.")
    
#     Island = input("Type wait to wait for a boat. Type swim to swim across.\n").lower()
#     if Island == "wait":
#         print("You arrived at the island unharmed. There is a house with 3 doors")

#         house = input("One red, one yellow and one blue. Which color do you choose?\n").lower()
#         if house == "red":
#             print("It's a room full of fire. Game Over.")
#         elif house =="blue":
#             print("You enter a room of beasts. Game Over.")
#         elif house == "yellow":
#             print("You found the treasure! You Win!")
#     elif Island == "swim":
#         print("You get attacked by an angry trout. Game Over.")
#     else:
#         print("Wrong input. Run again")
# elif Cross_road == "right":
#     print("You fell into a hole. Game over")
# else:
#     print("Wrong input. Run again")

# print("Thankyou for playing, Play again")

# ! Gemini code

#! Day 3 Final Project - Treasure Island
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# # Use .lower() so "LEFT" and "left" both work
# choice1 = input('You\'re at a cross road. Type "left" or "right": ').lower()

# if choice1 == "left":
#     # Level 2
#     choice2 = input('You\'ve come to a lake. Type "wait" or "swim": ').lower()
#     if choice2 == "wait":
#         # Level 3
#         choice3 = input("Which door? Red, Blue, or Yellow: ").lower()
#         if choice3 == "red":
#             print("Burned by fire. Game Over.")
#         elif choice3 == "blue":
#             print("Eaten by beasts. Game Over.")
#         elif choice3 == "yellow":
#             print("You Win!")
#         else:
#             print("Game Over. That door doesn't exist.")
#     else:
#         print("Attacked by trout. Game Over.")
# else:
#     print("Fell into a hole. Game Over.")