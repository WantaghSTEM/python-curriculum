# Credit for the vast majority of the code:
# https://gist.github.com/DevDarren/4199441
# DevDarren

import random


class Hangman():

    def __init__(self):
        print "Welcome to 'Hangman'!"
        print "(type the number 1) Yes, bring it on!\n(type the number 2) No, get me outta here!"
        user_choice_1 = raw_input("->")

        if user_choice_1 == '1':
            print "Loading..."
            self.start_game()
        elif user_choice_1 == '2':
            print "Bye bye now..."
            exit()
        else:
            print "I'm sorry, I'm hard of hearing, could you repeat that?"
            self.__init__()

    def start_game(self):
        print "Welcome to Hangman! If you make 6 wrong guesses, you lose!"
        print "If you think you know the full word, type it out completely."
        print "If you're correct, then you win! Else, you automatically lose!"
        print "Good luck!"
        self.core_game()

    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = random.choice(["pizza", "chow", "funny"])
        progress = ["?"] * len(the_word)

        while guesses <= 6:
            guess = raw_input("Guess a letter -> ")

            if len(guess) > 1:
                if guess == the_word:  # when the user wins
                    print " "
                    # ********* PROBLEM #3 :: Is this in the right place? ***
                    print "You've tried to guess the whole word!"
                    print "Sadly, you were wrong... You lose!"
                    print " "
                    quit()
                else:  # when the user loses
                    print " "
                    # ********* PROBLEM #3 :: Is this in the right place? ***
                    print "Congrats you've won!"
                    print "Come back soon!"
                    print " "
                    quit()
            else:
                if guess in the_word:
                    if guess not in letters_used:
                        print "As it turns out, your guess was RIGHT!"
                        letters_used += "," + guess
                        self.hangman_graphic(guesses)
                        print "Progress: " + self.progress_updater(guess, the_word, progress)
                        print "Letter used: " + letters_used
                        if list(the_word) == progress:
                            print " "
                            print "Congrats you've won!"
                            print "Come back soon!"
                            print " "
                            quit()
                elif guess not in the_word:
                    if guess not in letters_used:
                        guesses = 0  # *************************** PROBLEM #1 :: Why is it not changing?  ***
                        print "Things aren't looking so good, that guess was WRONG!"
                        letters_used += "," + guess
                        self.hangman_graphic(guesses)
                        print "Progress: " + "".join(progress)
                        print "Letter used: " + letters_used
                else:
                    print "That's the wrong letter, you wanna be out here all day?"
                    print "Try again!"

    def hangman_graphic(self, guesses):
        if guesses == 0:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /       "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|             "  # *************** PROBLEM #2 :: something is missing here... ***
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     / \     "
            print "|             "
            print "GAME OVER!"
            self.__init__()

    def progress_updater(self, guess, the_word, progress):
        for i in range(0, len(the_word)):
            if guess == the_word[i]:
                progress[i] = guess
        return "".join(progress)

game = Hangman()
