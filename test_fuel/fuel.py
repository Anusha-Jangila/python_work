def main():
    while True:
        fraction = input("Fraction: ")
        percent = 0
        try:
            percent = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(gauge(percent))


def convert(fraction):
    x, y = fraction.split('/')

    if not (x.isnumeric() and y.isnumeric()):
        raise ValueError

    int_x = int(x)
    int_y = int(y)

    if int_y == 0:
        raise ZeroDivisionError

    if int_x > int_y:
        raise ValueError

    percent = (int_x/ int_y) * 100
    return int(round(percent, 0))


def gauge(percentage):
    if (percentage <= 1):
        return("E")
    elif (99 <= percentage <= 100):
        return("F")
    elif (percentage <= 100):
        return(f"{percentage}%")



if __name__ == "__main__":
    main()