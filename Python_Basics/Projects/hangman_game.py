# First we choose a random word from the 01_Hangman_words.txt file.
# Let's set a rule for chosen word length. The length of the word should be at least 5 and not more than 8.
# This will make the game a bit harder but that's what we play games for.

import random


def get_a_random_word():
    word_lst = []
    with open("hangman_words.txt", "r") as words_txt:
        words = words_txt.readlines()
        for word in words:

            # replacing the leading and trailing quote sign as well as comma if present
            to_remove = ['"', ","]
            word = word.strip()
            for x in to_remove:
                word = word.replace(x, "")

            # appending the cleaned word to a list if, 5 <= length <= 8
            if len(word) >= 5 and len(word) <= 8:
                word_lst.append(word)

        # now returning a randomly chosen word
        return random.choice(word_lst)


# importing the python file containing the visuals

from hangman_visual import game_progress_remaining_lives_visual_dict as visual


# Now we write the actual logic of the game

# Initial Visual and Chit-chat
def initial():
    word = get_a_random_word().upper()
    lives = 6

    # first visual of the game
    print("This is the gallows were you would be hanged if you were to fail!")
    print(visual[lives])

    # initial chit-chat
    if len(word) > 6:
        print("Tough luck.")
    print("The randomly selected word has {} characters in it.".format(len(word)))
    print("\n")
    print("Word Progress: ", "#" * len(word))
    print("\n")
    print("You can guess wrong only {} times. So, Be Careful!".format(lives))
    print("Are you ready?")
    print("\n")
    return [word, lives]


# Importing the regex library to check if the user input is valid or not
import re


# Guess
def guess():
    print("<<<<00000000000000000000000000000000000000000>>>>")
    guessed_char = str(input("Please enter Your guess (A-Z):")).strip().upper()

    # re.findall returns an empty list if not matched
    validity = re.findall("^[a-z]$", guessed_char) or re.findall(
        "^[A-Z]$", guessed_char
    )
    if len(validity) == 0:
        print(
            "Either there are more than one alphabet or the input is not an alphabet at all! Please provide a valid input."
        )
        guess()
    else:
        return guessed_char


# User inputs list and progress string list is defined here
# so as not to initialize all over again when progress function is called.
# Remember not to initialize empty variables i.e, lists, strings etc
# inside a function unless you are absolutely sure about what you are doing

# Game Progress
def progress(usr_input, word_elements, lives, progress_string_elements):
    # Prevent entering the same Alphabet twice
    if usr_input in usr_inputs:
        print(
            "You have already guessed this Alphabet before. Guess a new one. Your life was not reduced this time around but there's no promise for the next time!"
        )
        play(word_elements, lives, progress_string_elements)

    # appending already inputted alphabets to the user inputs list
    usr_inputs.append(usr_input)

    # progress string
    progress_string = "".join(progress_string_elements)

    # Display progress
    def display_progress():
        print(f"\nLives left: {lives}")
        print(f"\nGame progress: {progress_string}")
        print(f"\nAlready guessed Alphabets: {usr_inputs}")
        print(f"\nVisual: {visual[lives]}")

    # checking whether the guessed alphabet is actually in the chosen word
    # and displaying the overall progress till now
    if usr_input in word_elements:
        print(
            "Well, Well! Would you look at that! Your guessed alphabet is indeed present in the word."
        )

        for i in range(len(word_elements)):
            if usr_input == word_elements[i]:
                progress_string_elements[i] = f"{usr_input}"

        progress_string = "".join(progress_string_elements)

        display_progress()

    if usr_input not in word_elements:
        print("Your guessed Alphabet is not present in the word.")
        lives = lives - 1
        display_progress()

    return [lives, progress_string_elements]


def play(word_elements, lives, progress_string_elements):
    # Elements in the chosen word
    word_elements = word_elements
    # user guessed
    usr_input = guess()

    # Game progress after a guess
    game_progress = progress(usr_input, word_elements, lives, progress_string_elements)

    updated_lives = game_progress[0]
    updated_progress_string_elements = game_progress[1]

    # Until lives becomes 0 continue the game
    if updated_lives > 0:

        # Winning condition
        if "".join(updated_progress_string_elements) == "".join(word_elements):
            print("Congratulations! YOU WON!")

        # Otherwise continue
        else:
            play(word_elements, updated_lives, updated_progress_string_elements)
    else:
        print("Game over. You are hanged!")
        print("The word was: {}".format(" ".join(word_elements)))


initiate = initial()
word = initiate[0]
lives = initiate[1]

# initial user inputs list
usr_inputs = []

# initial Progress string to be displayed
display_string_progress = []

word_elements = [word[i] for i in range(len(word))]

for i in range(len(word_elements)):
    display_string_progress.append("#")

progress_string = "".join(display_string_progress)
progress_string_elements = [progress_string[i] for i in range(len(progress_string))]

# Cheating
# print(word)

play(word_elements, lives, progress_string_elements)
