# print ("Hello")
# def greet():
#     print ("Hello\nHow do You do")

# greet()

# ! function that allows for inputs

# def greet_with_name(name):
#     print (f"Hello {name}\nHow do You do {name}")

# greet_with_name("Angela")

# ! fuctions with more than 1 input

# def greet_with(name, location):
#     print (f"Hello {name}\nWhat is it like in {location}")

# greet_with("Jack", "Tortuga")

# ! Keyword arguments
# greet_with(location= "Tortuga", name= "Jack")

# ! love calculator with loop
# def calculate_love_score(name1, name2):
#     combined_name = (name1 + name2).lower()
#     true_count = 0
#     love_count = 0
#     for letter in combined_name:
#         if letter in "true":
#             true_count += 1
#         if letter in "love":
#             love_count += 1
    
#     print (str(true_count)+ str(love_count))

# calculate_love_score("Kanye West", "Kim Kardashian")

# ! love calculator with count
# def calculate_love_score(name1, name2):
#      combined_string = (name1 + name2).lower()
#      t = combined_string.count("t")
#      r = combined_string.count("r")
#      u = combined_string.count("u")
#      e = combined_string.count("e")
#      true_total = t + r + u + e
    
#      l = combined_string.count("l")
#      o = combined_string.count("o")
#      v = combined_string.count("v")
#      e = combined_string.count("e")
#      love_total = l + o + v + e
    
#      print(f"{true_total}{love_total}")

# calculate_love_score("Kanye West", "Kim Kardashian")

# ! Caesar Cipher Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
            else:
                shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")