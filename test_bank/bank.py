def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    strToCompare = greeting.casefold().lstrip()
    if(strToCompare.startswith('hello')):
        return 0
    elif(strToCompare.startswith('h')):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


