import sys
from random import choice
from pyfiglet import Figlet

def print_figlet(f):
    figlet = Figlet()
    validFonts = figlet.getFonts()
    if (f == ""):
        f = choice(validFonts)
    if not f in validFonts:
        sys.exit("Invalid usage")
    figlet.setFont(font=f) #sys.argv[2]
    str = input("Input: ")
    print(figlet.renderText(str))

if not (len(sys.argv) == 1 or len(sys.argv) == 3):
    sys.exit("Invalid usage")

if (len(sys.argv) == 1):
    print_figlet("")

elif (len(sys.argv) == 3):
    if not (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        sys.exit("Invalid usage")
    print_figlet(sys.argv[2])
