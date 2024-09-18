import sys

if(len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")

if(len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1].rstrip()
if not (file_name.endswith(".py")):
    sys.exit("Not a python file")

line_count = 0
try:
    with open(file_name) as file:
        for line in file:
            line = line.lstrip()
            if not (len(line) == 0 or line.startswith("#")):
                line_count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(line_count)
