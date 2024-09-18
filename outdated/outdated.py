months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()
    try:
        if date[0].isalpha():
            [month, date, year] = date.split()
            if month not in months:
                continue
            month = months.index(month) + 1
            if not date.endswith(','):
                continue
            date = int(date.rstrip(','))
            if not (1 <= date <= 31):
                continue
        else:
            [month, date, year] = date.split('/')
            if not (1 <= int(month) <= 12 and 1 <= int(date) <= 31 and len(year) == 4):
                continue
            month = int(month)
            date = int(date)

        print(f"{year}-{month:02}-{date:02}")
        break
    except ValueError:
        pass

