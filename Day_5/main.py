import random
# ! Beginner Python Loops

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(f"{fruit} pie")

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 98, 66, 87, 79, 84, 96, 97,92, 74]

# print(sum(student_scores))
# print(98 + 78)
# print(max(student_scores))

#*sum using loop
# sum = 0                       
# for score in student_scores:
#     sum += score
# print(sum)

#* max using loop
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
#     else:                              #* her even if you don't use the else statement it doesn't going to change the outcome. Why?
#         max_score = max_score
# print(max_score)

# ! for loops and the range function

# * range function is used in conjunction

# for number in range(1,10,2):  #* doesn't take the last number in printing
#     print(number)

# sum = 0
# for number in range(1,101):
#     sum += number
# print(sum)

# ! Fizz Buzz Challenge

# for number in range(1, 101):
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# ! Password Generator

# ! Easy mode 

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator !")
# no_of_letters = int(input("How many lettes would you like in your password?\n"))
# no_of_symbols = int(input("How many symbols would you like in your password?\n"))
# no_of_numbers = int(input("How many numbers would you like in your password?\n"))

# password = ""
# for no_of_letter in range(0, no_of_letters):
#     password += random.choice(letters)
    
# for no_of_symbol in range(0, no_of_symbols):
#     password += random.choice(symbols)

# for no_of_number in range(0, no_of_numbers):
#     password += random.choice(numbers)

# print(password)

# ! Hard mode

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator !")
no_of_letters = int(input("How many lettes would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like in your password?\n"))
no_of_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []
for no_of_letter in range(0, no_of_letters):
    password_list.append(random.choice(letters)) 
    
for no_of_symbol in range(0, no_of_symbols):
    password_list.append(random.choice(symbols))

for no_of_number in range(0, no_of_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")