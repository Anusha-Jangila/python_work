import sys
import csv
from tabulate import tabulate

if(len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")

if(len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]
if not (file_name.endswith(".csv")):
    sys.exit("Not a CSV file")

try:
    with open(file_name) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers = "keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
