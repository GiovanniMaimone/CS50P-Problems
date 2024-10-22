import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

font = figlet.getFonts()

if len(sys.argv) == 1 :
    userandomfont = True

elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in font:
    userandomfont = False
    spefont = sys.argv[2]

else:
    sys.exit("Invalid usage")

input = input("Input: ")

if userandomfont == True:
    randomfont = random.choice(figlet.getFonts())
    print(figlet.renderText(input))

else:
    setfont = figlet.setFont(font=spefont)
    print(figlet.renderText(input))
