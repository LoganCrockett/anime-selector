'''
Add Anime to List Menu
@author LoganCrockett
'''
def displayAddAnimeToListMenu():
    print("\nAdd Anime to List\n")
    print("Please enter the name of each anime one at a time, and press enter.")
    print("When finished, type 'q' to stop adding entries\n")

    askForUserInput = True
    while askForUserInput:
        try:
            userInput = input("Anime Name:")
            print(userInput)

            if userInput == 'q' or userInput == 'Q':
                askForUserInput = False
        except KeyboardInterrupt:
            askForUserInput = False

    print("\n")