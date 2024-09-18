user_input = input("Input: ")
output_str = ""
for letter in user_input:
    if(letter not in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']):
        output_str += letter

print("Output: "+ output_str)