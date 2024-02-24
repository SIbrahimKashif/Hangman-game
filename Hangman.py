import random
from words import *  # custom words list

while True:
    # get a random word from the list
    category_mapping = {
        "cars": cars,
        "tech companies": tech_companies,
        "countries": countries,
        "social media": social_media,
    }

    category = random.choice(list(category_mapping.keys()))
    acategory = category_mapping[category]

    word = random.choice(acategory)

    errors = 0
    letters = len(word)
    guessed = []  # contains all the letters correctly guessed by the player
    tried = []  # contains all the letters tried by the player

    unique_letters = set(word)

    print(f"\nCategory: {category}")
    print("_ " * letters)

    while True:
        # random variables
        tries_left = len(unique_letters) - errors
        tries = "try" if errors == 1 else "tries"
        triesLeft = "try" if tries_left == 1 else "tries"

        # take user input for a guess
        guess = input("\nGuess a letter: ").lower()
        tried.append(guess)

        # to check if the guess is a single alphabetic letter
        if len(guess) == 1 and guess.isalpha():
            # if guess is correct and hasnt already been guessed
            if guess in word and guess not in guessed:
                guessed.append(guess)
                print()

                for letter in word:
                    if letter in guessed:
                        print(letter, end="")
                    else:
                        print("_", end="")
                print()

                # check for win
                if sorted(guessed) == sorted(unique_letters):
                    print(f"\nYou win :) with {errors} {tries} wrong.\n")
                    break
            else:
                # if letter is not already tried
                if tried.count(guess) <= 1:
                    errors += 1
                    if tries_left > 0:
                        print(
                            f"\nIncorrect letter, You have {tries_left} {triesLeft} left"
                        )

                    # check for lose
                    if tries_left <= 0:
                        print(f"\nYou lose :( with {errors} tries wrong.\n")
                        print(f"Correct answer: {word}\n")
                        break
                else:  # if letter is already guessed or tried
                    used = "guessed" if guess in guessed else "tried"
                    print(f"\nYou have already {used} this letter")

        # hint keyword
        elif guess == "hint":
            remaining_letters = [letter for letter in word if letter not in guessed]

            hint_letter = random.choice(remaining_letters)
            print(f"\nThe word contains the letter: {hint_letter}")

        else:
            print("\nYou are only allowed to enter a letter")

    # give user option to play again or close game when game ends
    quit = input("Press enter to play again or press q to quit ").lower()

    if quit == "q":
        break
