def main():
    str = input("What time is it? ")
    time = convert(str)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    meridian = ""
    if(time.find(" ") != -1):
        time, meridian = time.split(" ")

    #time -- "7:30"
    #floatTime -- 7.5
    hours, minutes = time.split(":")

    iHour = int(hours)
    if(meridian == "p.m."):
        iHour = iHour + 12
    fMinutes = float(minutes)/60
    floatTime = iHour + fMinutes
    return floatTime


if __name__ == "__main__":
    main()

