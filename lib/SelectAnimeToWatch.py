from lib.AnimeRecord import AnimeRecord
from lib.ClearScreen import clearScreen
import random, msvcrt

'''
Select Anime to Watch Menu
@author LoganCrockett
'''
def displaySelectAnimeToWatchMenu():
    if len(AnimeRecord.currentWatch) > 0:
        print("You are currently watching '" + AnimeRecord.currentWatch + "'. Please mark it as complete before selecting a new anime.\n")
        return
    
    toWatchList = list(AnimeRecord.toWatch)
    toSelectList = list()
    if len(toWatchList) == 0:
        print("No entries found in the to watch list. Please add some titles before selecting\n")
        return
    elif len(toWatchList) == 1:
        AnimeRecord.setCurrentWatch(toWatchList[0])
        print("Current watch is now: " + AnimeRecord.currentWatch)
        print()
        return
    elif len(toWatchList) == 2 or len(toWatchList) == 3:
        toSelectList = toWatchList
    else:
        userIndex = 0
        clearScreen()
        print("Please select three items to put up for selection (Use W/S to navigate)")
        while len(toSelectList) < 3:
                indicesToDisplay = []
                if len(toWatchList) > 2:
                    if userIndex == 0:
                        indicesToDisplay = [0, 1, 2]
                    elif userIndex == len(toWatchList) - 1:
                        indicesToDisplay = [len(toWatchList) - 3, len(toWatchList) - 2, len(toWatchList) - 1]
                    else:
                        indicesToDisplay = [userIndex - 1, userIndex, userIndex + 1]
                else:
                    # If we end up selecting, and the list dips below three
                    indicesToDisplay = list(range(len(toWatchList)))
                
                for i in indicesToDisplay:
                    print("-> " if i == userIndex else "", toWatchList[i])

                try:
                    # See https://stackoverflow.com/a/61560100 for getting arrow keys on Windows
                    # Block here so that we don't constantly print out the options
                    while msvcrt.kbhit() == False:
                        pass
                    userInput = msvcrt.getch()

                    # Read second character to get arrow
                    if userInput == b'\x00':
                        userInput = msvcrt.getch()

                    # Pressed Enter
                    if userInput == b'\r':
                        toSelectList.append(toWatchList.pop(userIndex))

                        if userIndex > len(toWatchList) - 1:
                            userIndex -= 1
                    elif userInput == b'H':
                        userIndex = len(toWatchList) - 1 if userIndex == 0 else userIndex - 1
                    elif userInput == b'P':
                        userIndex = (userIndex + 1) % len(toWatchList)
                except KeyboardInterrupt:
                    # Just exit; stop processing
                    print("Exiting selection and returning to main menu\n")
                    return
                finally:
                    clearScreen()


    print("Current items up for selection: " + str(toSelectList))
    print("Press enter when you are ready to select")
    input()

    AnimeRecord.setCurrentWatch(random.choice(toSelectList))
    print("Current watch is now: " + AnimeRecord.currentWatch)
    print()
    return
