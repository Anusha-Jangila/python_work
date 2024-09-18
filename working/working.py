import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #convert 12 hr format to 24 hr format
    # input:
    #       9:00 AM to 5:00 PM
    #       9 AM to 5 PM
    # output:
    #       9:00 to 17:00
    if matches:= re.search("^([0-9]{1,2})+(?::)?([0-9]{0,2}) (AM|PM) to ([0-9]{1,2})+(?::)?([0-9]{0,2}) (AM|PM)$", s):
        starting_meridian = matches.group(3)
        ending_meridian = matches.group(6)

        starting_hour = int(matches.group(1))
        starting_minutes = 0
        if matches.group(2) != "":
            starting_minutes = int(matches.group(2))

        ending_hour = int(matches.group(4))
        ending_minutes = 0
        if matches.group(5) != "":
            ending_minutes = int(matches.group(5))

        if (1 <= starting_hour <= 12 and 0 <= starting_minutes <= 59 and
            1 <= ending_hour <= 12 and 0 <= ending_minutes <= 59):
            if starting_meridian == "PM":
                starting_hour = starting_hour + 12
            if ending_meridian == "PM":
                ending_hour = ending_hour + 12

            # 12:00 AM --> 00:00
            if starting_hour == 12:
                starting_hour = 0
            # 12:00 PM --> 12:00
            if ending_hour == 24:
                ending_hour = 12

            return f"{starting_hour:02}:{starting_minutes:02} to {ending_hour:02}:{ending_minutes:02}"

    raise ValueError



if __name__ == "__main__":
    main()