from random import *

# Constants
FILENAME = "words"
FAREWELL_MESSAGE = "Thank you for playing! :)"
WELCOME_MESSAGE = "Welcome to Acak Kata! Preparing words..."
MAX_GUESS = 10

# Scramble a word
def scramble(s):
    list_characters = list(s)
    shuffle(list_characters)
    return "".join(list_characters)

# Main function
if __name__ == "__main__":
    print WELCOME_MESSAGE

    with open(FILENAME) as f:
        wordlist = f.read().split()

        playing = True

        # Start the game loop
        while playing:
            word = wordlist[randint(0, len(wordlist) - 1)].lower() # Select a random word from the dictionary
            scrambled_word = scramble(word) # Scramble the word

            print "Word to guess:", scrambled_word

            guesses_left = MAX_GUESS
            correct = False

            # Player's turn to guess
            while guesses_left > 0 and not(correct):
                guess = raw_input("Your guess: ")

                if guess == word:
                    correct = True
                    print "Correct!"
                else:
                    guesses_left -= 1

                    if guesses_left == 0:
                        print "Wrong! The correct answer is:", word
                    else:
                        print "Wrong! Number of guesses left:", guesses_left

            play_again = ""

            while play_again != "YES" and play_again != "NO":
                play_again = raw_input("Play again? [YES/NO] ").upper()

            if play_again == "NO":
                playing = False

    print FAREWELL_MESSAGE
