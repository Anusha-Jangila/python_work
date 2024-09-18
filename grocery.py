groceries = {} # Declaring groceries dict
while True: # Keep on accepting inputs
    try:
        item = input()
        if item in groceries: # If entered item found in groceries dict, increase the associated count by 1
            groceries[item] += 1
        else:
            groceries[item] = 1 # Else, add as a new item
    except EOFError: # When Ctrl-D is hit
        print("")
        sorted_groceries_list = sorted(groceries)
        # result: [APPLE, BANANA, CHERRY]
        for grocery in sorted_groceries_list:
            print(groceries[grocery], grocery.upper(), sep = " ")
        break
