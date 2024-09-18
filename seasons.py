from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")

    # Validate DOB
    if validate_dob(dob):
        # Convert string DOB to date
        dob = convert_to_date(dob)
        # Get age in minutes
        minutes = age_in_minutes(dob)
        words = p.number_to_words(minutes, andword="")
        print(words[0].upper() + words[1:] + " minutes")
        sys.exit()

    sys.exit("Invalid date")

def validate_dob(dob):
    if matches := re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", dob):
       return True
    return False

def convert_to_date(dob):
    year, month, dt = dob.split("-")
    year = int(year)
    month = int(month)
    dt = int(dt)
    return date(year, month, dt)

def age_in_minutes(dob):
    today = date.today()
    diff = today - dob
    return diff.days * 24 * 60

if __name__ == "__main__":
    main()
