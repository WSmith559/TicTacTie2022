from Ui import Gui, Terminal
from sys import argv

def usage():   
    print(f"""
Usage: {argv[0]} [g | t]
g : play with the GUI
t : play with the Terminal""")
    quit()

if __name__ == "__main__":
    if len(argv) != 2:
        usage()
    elif argv[1] == "t":
        Ui = Terminal()
    elif argv[1] == "g":
        Ui = Gui()
    else:
        usage()
    
    #polymorphism being used

