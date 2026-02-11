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

