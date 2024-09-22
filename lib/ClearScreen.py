from os import system, name
# "Generously donated" from https://www.geeksforgeeks.org/clear-screen-python/
def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")