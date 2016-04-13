from random import *

# Constants
FILENAME = "words"
FAREWELL_MESSAGE = "Thank you for playing! :)"
WELCOME_MESSAGE = "Welcome to Acak Kata! Preparing words..."

INF = 2000000
MAX_GUESS = 10
MIN_WORD_LENGTH = {"EASY": 2, "MEDIUM": 6, "HARD": 11}
MAX_WORD_LENGTH = {"EASY": 5, "MEDIUM": 10, "HARD": INF}

DIFFICULITIES = ["EASY", "MEDIUM", "HARD"]

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

        # Choose difficulity first
        difficulity = ""
        while difficulity not in DIFFICULITIES:
            difficulity = raw_input("Select your difficulity (EASY / MEDIUM / HARD): ").upper()

        min_length = MIN_WORD_LENGTH[difficulity]
        max_length = MAX_WORD_LENGTH[difficulity]

        playing = True

        # Start the game loop
        while playing:
            # Select a random word from the dictionary
            word = wordlist[randint(0, len(wordlist) - 1)].lower()
            while not(min_length <= len(word) <= max_length):
                word = wordlist[randint(0, len(wordlist) - 1)].lower()

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
