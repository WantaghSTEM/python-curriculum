# teacher master copy
# Random Password Generator
import random

# Ask the user how long he/she wants their password to be:
desired_length = int(
    raw_input("How many characters long would you like your password to be? >> "))

# What should our password start as? (Hint: An empty string.)
password = ""

# What is the current length of our password? (Hint: It has no length.)
current_length = 0

# Write a while-loop that runs up until our password is as long as desired length:
#   (Hint: The [condition] should be true when the current_length of the password
#    is less than the desired_length of the password.)
while current_length < desired_length:
    # We're giving this to you. This line of code chooses a random character:
    random_character = random.choice(
        "abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ1234567890!@#$%&")
    # Add the random_character to our password:
    password = password + random_character
    # What is the current_length of our password?
    #   (Hint: It is 1 character longer than it previously was.)
    current_length = current_length + 1

# print the password:
print password
