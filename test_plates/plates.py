def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def starts_with_2letters(s):
    #All vanity plates must start with at least two letters
    return s[0:2].isalpha()

def is_length_valid(s):
    #vanity plates may contain a maximum of 6 characters and a minimum of 2 characters.
    return 2 <= len(s) <=6

def is_format_valid(s):
    #Numbers cannot be used in the middle of a plate; they must come at the end.
    #The first number used cannot be a ‘0’.
    for char in s:
        if char.isnumeric():
            if(char == '0'):
                return False
            i = s.index(char)
            j = len(s)
            if s[i:j].isnumeric():
                return True
            else:
                return False
    return True

def has_no_special_chars(s):
    #No periods, spaces, or punctuation marks are allowed
    return s.isalnum()

def is_valid(s):
    return (starts_with_2letters(s) and
            is_length_valid(s) and
            is_format_valid(s) and
            has_no_special_chars(s))

if __name__ == "__main__":
    main()