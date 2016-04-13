from random import *

# Constants
FILENAME = "words"
FAREWELL_MESSAGE = "Thank you for playing! :)"
WELCOME_MESSAGE = "Welcome to Acak Kata! Preparing words..."

INF = 2000000
MAX_GUESS = 10

# Minimum word length, maximum word length, and base score for each difficulity
SETTINGS = {"EASY": (2, 5, 10), "MEDIUM": (6, 10, 20), "HARD": (11, INF, 40)}

DIFFICULITIES = ["EASY", "MEDIUM", "HARD"]

# Scramble a word
def scramble(s):
    list_characters = list(s)
    shuffle(list_characters)
    return "".join(list_characters)

# Main function
if __name__ == "__main__":
    print WELCOME_MESSAGE

    # Retrieve the wordlist from a text file
    wordlist = list()
    with open(FILENAME) as f:
        wordlist = f.read().split()

    # Choose difficulity first
    difficulity = ""
    while difficulity not in DIFFICULITIES:
        difficulity = raw_input("Select your difficulity (EASY / MEDIUM / HARD): ").upper()

    min_length, max_length, base_score = SETTINGS[difficulity]

    playing = True
    total_score = 0

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
                total_score += base_score * guesses_left
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

    print "Your total score:", total_score
    print FAREWELL_MESSAGE
