# If 1, 2 or 3 is not enetered, prompt again
# Randomly generate 10 math problems
# Validate the input, print EEE for error; after 3 chances output correct answer
# Output user's score

import random


def main():
    count = 10
    score = 0

    level = get_level()
    while count > 0:
        value_error = False
        try:
            a = generate_integer(level)
            b = generate_integer(level)
            expected_result = a + b
            try:
                inputted_result = int(input(f"{a} + {b} = "))
            except ValueError:
                value_error = True

            if inputted_result != expected_result or value_error:
                error_count = 2
                while error_count > 0:
                    print("EEE")
                    try:
                        inputted_result = int(input(f"{a} + {b} = "))
                    except ValueError:
                        error_count = error_count - 1
                        continue
                    if inputted_result == expected_result:
                        break
                    error_count = error_count - 1
                if error_count == 0:
                    print(f"{a} + {b} = {expected_result}")
            else:
                score = score + 1

            count = count - 1
        except ValueError:
                continue

    print("Score:" , score)



def get_level():
    # Prompt the user for a level
    while True:
        str_level = input("Level: ")
        try:
            int_level = int(str_level)
        except ValueError:
            continue
        if int_level == 1 or int_level == 2 or int_level == 3:
            return int_level

# returns a randomly generated non-negative integer with level digits
# or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    if not (level == 1 or level == 2 or level == 3):
        raise ValueError
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
