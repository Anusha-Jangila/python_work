import sys
import csv

if(len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")

if (len(sys.argv) > 3):
    sys.exit("Too many command-line arguments")

existing_file_name = sys.argv[1] #name, house
new_file_name = sys.argv[2] #first, last, house

try:
    with open(existing_file_name) as file:
        reader = csv.DictReader(file)
        with open(new_file_name, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                name = row["name"]
                house = row["house"]
                last, first = name.split(",")
                last = last.strip()
                first = first.strip()
                writer.writerow({"first":first, "last":last, "house":house})
except FileNotFoundError:
    sys.exit("Could not read " + existing_file_name)


