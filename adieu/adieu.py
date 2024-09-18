import inflect
p = inflect.engine()

names = ()
while True:
  try:
    # prompt for names
    name = input("Name: ")
    # Add strings to the tuple ("str1","str2",..)
    names += (name,)
  # until EOFError
  except EOFError:
    # call inflect.join on the strings
    list_of_names = p.join(names)
    print("")
    # Display the result
    print("Adieu, adieu, to "+ list_of_names)
    break
