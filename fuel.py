while True:
    fraction = input("Fraction: ")
    percent = 0
    try:
        x, y = fraction.split('/')
        int_x = int(x)
        int_y = int(y)
        percent = (int_x/ int_y) * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if (percent <= 1):
            print("E")
            break
        elif (99 <= percent <= 100):
            print("F")
            break
        elif (percent <= 100):
            print(f"{percent:.0f}%")
            break
