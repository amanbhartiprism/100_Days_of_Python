# print("Hello world")/
# Creating a dictionary
# programming_dictionary = {
#     "Bug": "An error in a program that prevents it from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# Looking up an item (Using the Key)
# print(programming_dictionary["Bug"])

# /adding up an item
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# 4. EDITING AN EXISTING ITEM
# -------------------------------------------------------------------------
# If the key already exists, Python overwrites its value
# programming_dictionary["Bug"] = "A moth in your computer causing chaos."

# 5. CREATING AN EMPTY DICTIONARY / WIPING AN EXISTING ONE
# -------------------------------------------------------------------------
# empty_dictionary = {}
# To wipe an existing dictionary, you would uncomment the line below:
# programming_dictionary = {}

# 6. LOOPING THROUGH A DICTIONARY
# -------------------------------------------------------------------------
# By default, a for loop only gives you the KEYS
# for key in programming_dictionary:
#     print(key)                      # Prints: Bug, Function, Loop
#     print(programming_dictionary[key])  # Prints the corresponding definition string

# -------------------------------------------------------------------------
# TYPE A: Nesting a List inside a Dictionary
# -------------------------------------------------------------------------
# travel_log_v1 = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# -------------------------------------------------------------------------
# TYPE B: Nesting a Dictionary inside a Dictionary
# -------------------------------------------------------------------------
# travel_log_v2 = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visits": 5},
# }

# -------------------------------------------------------------------------
# TYPE C: Nesting Dictionaries inside a List (The Core Industry Standard)
# -------------------------------------------------------------------------
# travel_log_v3 = [
#     {
#         "country": "France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "country": "Germany", 
#         "cities_visited": ["Berlin", "Hamburg"], 
#         "total_visits": 5
#     },
# ]

# -------------------------------------------------------------------------
# THE SECRET AUCTION PROGRAM
# -------------------------------------------------------------------------

# Dictionary to hold all user bids: {"Name": BidAmount}
# bids = {}
# auction_active = True

# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
    
#     # Loop through the dictionary keys to evaluate values
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
            
#     print(f"The winner is {winner} with a bid of ${highest_bid}")

# # Main execution loop
# while auction_active:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
    
#     # Save the input data into our bids dictionary
#     bids[name] = price
    
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
#     if should_continue == "no":
#         auction_active = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         # VS Code console clear trick (prints 20 empty lines to hide previous inputs)
#         print("\n" * 20)