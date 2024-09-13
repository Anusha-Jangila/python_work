user_input = input("camelCase: ")
snake_case = ""
for letter in user_input:
  if letter.isupper():
    snake_case += "_"
    letter = letter.lower()
  snake_case += letter
print("snake_case: "+snake_case)
