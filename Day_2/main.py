# print(len("hello"))
# print("Hello"[0])
# print("Hello"[4])
# print("Hello"[-1])
# you can't do ("123" + "345") for mathematical operation as it takes as string, it simply just concatenates

# Integer = Whole number
# print(123 + 345)

# Large Integers
# print(124_123_233)

# Float = Floating Point Number
# print(34.4566)

# Boolean
# print(True)
# print(False)

# function process like a french fries machine
# len(12345) it won't work
# print(len("12345") ) #* it will work as a string

# check the data-type
# print(type("hello"))
# print(type(123))
# print(type(123.12))
# print(type(False))
# print("hello" + type("hello")) TypeError: can only concatenate str (not "type") to str

# ! Type Conversion

# int("123") #*converting the string into int
# * you can convert in the same

# print(int("123") + int("345"))

# print("Number of letters in your name: " + str(len(input("Enter your name\n"))))

# ! Mathematical Operations

# print("My age" + str(24))
# print(123 + 345)
# print(7 - 3)
# print(2 * 3)
# print(6 / 3)  #* division will always give a float
# print(6 // 3) #* this gives a integer but it just don't give the values after point 
# print(3**2)  #* this is for exponents

# * PEMDAS rules apply here 
#* ()
#* **
#* * OR /
#* + OR - 
# print(3 * (3 + 3) / 3 - 3)

# ! Limiting the answer

# //weight = input("What is your weight") 
# //height = input("What is your height")
# * the upper one not working as input treats as string and later you cannot do mathematical operation on string
# weight = 84
# height = 1.65
# bmi = (weight / height ** 2)
# print(bmi)
# print(int(bmi))
# print(round(bmi)) #* using the round function
# print(round(bmi, 2))

# ! Assignment Operators

# score = 0
# #* User scores a point
# score += 1
# print(score)

# ! f - strings - uses for combining different data types as strings

# print("Your score is" + str(score))

# score = 0
# height = 1.8
# is_winning = True

# print(f"Your score is = {score}, your height is {height}. You are winning and that is {is_winning}")

# ! Final Project of the today

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $\n"))
tip = float(input("How much tip would you like to give? 10, 12 or 15\n"))
no_of_persons = int(input("How many people to split the bill?\n"))
bill_calculated = (total_bill + ((tip * total_bill) / 100 )) / no_of_persons
print(round(bill_calculated,2))