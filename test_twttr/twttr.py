def main():
    user_input = input("Input: ")
    print("Output: "+ shorten(user_input))


def shorten(word):
    output_str = ""
    for letter in word:
        if(letter not in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']):
            output_str += letter
    return output_str


if __name__ == "__main__":
    main()

