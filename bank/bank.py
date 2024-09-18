greeting = input("Greeting: ")
strToCompare = greeting.casefold().lstrip()
if(strToCompare.startswith('hello')):
  print("$0")
elif(strToCompare.startswith('h')):
  print("$20")
else:
  print("$100")
