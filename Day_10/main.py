# -------------------------------------------------------------------------
# 1. BASIC FUNCTION WITH AN OUTPUT (RETURN)
# -------------------------------------------------------------------------
# def format_name(f_name, l_name):
#     """Take a first and last name and format it 
#     to return the title case version of the name."""
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f_name.title() + " " + l_name.title()

# # Saving the output into a variable
# formatted_string = format_name("aNgElA", "yU")
# print(formatted_string) # Output: Angela Yu


# # -------------------------------------------------------------------------
# # 2. MULTIPLE RETURN STATEMENTS & EARLY EXIT
# # -------------------------------------------------------------------------
# def format_name_v2(f_name, l_name):
#     # Guard clause: Check if the user left an input blank
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
    
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f_name.title() + " " + l_name.title()

# print(format_name_v2("", "Yu")) # Output: You didn't provide valid inputs.


# -------------------------------------------------------------------------
# 3. THE CAPSTONE PROJECT: THE CALCULATOR
# -------------------------------------------------------------------------
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# # Storing functions inside a dictionary (Flags mapping), no triggering that's why we didn't use the brackets
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def calculator():
#     should_accumulate = True
#     num1 = float(input("What's the first number?: "))

#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What's the next number?: "))
        
#         # Grab the function from our dictionary based on the symbol key
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)
        
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
        
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ")
        
#         if choice == "y":
#             num1 = answer # Feed the answer back as the first number for the next round
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator() # RECURSION: The function calls itself to restart completely

# # Start the calculator program
# calculator()