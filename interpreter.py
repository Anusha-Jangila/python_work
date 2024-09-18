expression = input("Expression: ")
x, y, z = expression.split(" ")
match y:
    case "+":
        result = float(x) + float(z)
        print(f"{result:.1f}")
    case "-":
        result = float(x) - float(z)
        print(f"{result:.1f}")
    case "*":
        result = float(x) * float(z)
        print(f"{result:.1f}")
    case "/":
        result = float(x) / float(z)
        print(f"{result:.1f}")
