# This is a guess the number game.
import random # not explaining this

# Set a minimum and maximum value for the possible range
# *** step one: write definition of two variables below ***
minimum =
maximum =

# Chooses a random number between minimum and maximum values
number = random.randint(minimum, maximum)

# Ask for user's name
# *** step two: write print statement asking name below ***


# User writes in their name, code saves input as username
# *** step two: write definition of username as input below using raw_input() ***
username =

# Tells user the range of numbers to guess from
# *** step three: write print statement using maximum and minimum below ***
print username + ', I am thinking of a number between ' + str(minimum) + " and " + str(maximum)

# Counts the number of guesses so far, starting with none
guessesTaken = 0

# *** step four: write while loop and conditional below ***
while
    print 'Take a guess.'  # providing these four lines for you
    guess = raw_input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    # *** step five: create two if statements when guess is too low and too high below ***
    if
        print 'Your guess is too low.'
    if
        print 'Your guess is too high.'

    # ends the while loop when the user makes the correct guess
    if guess == number:
        break

# *** step six: create two if statements when guess is correct and incorrect ***
if
    guessesTaken = str(guessesTaken)
    print "Good job, " + username + "! You guessed my number in " + guessesTaken + " guesses!"

if
    number = str(number)
    print "Nope. The number I was thinking of was " + number

