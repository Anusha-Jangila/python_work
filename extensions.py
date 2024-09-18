fileName = input("File Name: ")
fileName = fileName.casefold().strip()
listOfStrings = fileName.split('.')
lengthOfList = len(listOfStrings)
extension = listOfStrings[lengthOfList - 1]
match extension:
    case "zip":
        print("application/zip")
    case "txt":
        print("text/plain")
    case "pdf":
        print("application/pdf")
    case "png":
        print("image/png")
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "gif":
        print("image/gif")
    case _:
        print("application/octet-stream")
