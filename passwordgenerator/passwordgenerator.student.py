# student copy
# Random Password Generator
import random

# Ask the user how long he/she wants their password to be:
desired_length = int(raw_input("  [replace me with a question]  "))

# What should our password start as? (Hint: An empty string.)
password =

# What is the current length of our password? (Hint: It has no length.)
current_length =

# Write a while-loop that runs until our password has the desired_length:
#   (Hint: The [some condition] should be true when the current_length of the
#    password is less than the desired_length of the password.)
while  # [some condition]
# We're giving this to you. This line of code chooses a random character:
    random_character = random.choice(
        "abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ1234567890!@#$%&")
    # Add the random_character to our password:
    password =
    # What is the current_length of our password?
    #   (Hint: It is 1 character longer than it previously was.)
    current_length =

# print the password:
