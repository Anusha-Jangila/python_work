inputByUser = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
inputByUser = inputByUser.lower().strip()
if(inputByUser=='42' or inputByUser=='forty-two' or inputByUser=='forty two')
    print("Yes")
else:
    print("No")
