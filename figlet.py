import pyfiglet
import sys
if len(sys.argv) == 1:
 random = pyfiglet.figlet_format(input("Input:"))
 print(random)
if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in pyfiglet.FigletFont.getFonts():
            sys_font = pyfiglet.figlet_format(input("Input:"),font=sys.argv[2])
            print(sys_font)
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')
