import random

while True:
    try:
        # prompt the user for level
        level = int(input("Level: "))
        # If not +ve int prompt again
        if level < 1:
            continue
        # use random.randint
        random_number = random.randint(1, level)
        break
    except ValueError:
        continue

while True:
    try:
        # Prompt to guess
        guessed_number = int(input("Guess: "))
        # If not +ve int guess again
        if guessed_number < 1:
            continue
        # Output Too large or Too small or Just right
        if guessed_number > random_number:
            print("Too large!")
            continue
        elif guessed_number < random_number:
            print("Too small!")
            continue
        else:
            print("Just right!")
        break
    except ValueError:
        continue


