def convert(str):
    str = str.replace(':)', '🙂')
    str = str. replace(':(', '🙁')
    return str


def main():
    inputByUser = input()
    print(convert(inputByUser))

main()
