# teacher master copy
# Tip Calculator

# Ask the user what their bill was:
bill_amount = int(raw_input("How much was your bill? >> "))

# Ask the user what percent they will tip their waiter with:
tip_percent = int(raw_input("With what percent would you like to tip? >> "))

# Multiply the tip_percent by the bill_amount:
#   (Note: As the user, will you enter the tip_percent as a
#    whole number or as a decimal?  We will assume as a whole number)
tip = bill_amount * tip_percent / 100

print "This is your tip:"
# print the tip on the next line:
print tip


print "This is the total amount you pay:"
# print the bill_amount plus the tip
print bill_amount + tip
