from lib.AddAnimeToListMenu import displayAddAnimeToListMenu
from lib.AnimeRecord import AnimeRecord
from lib.SelectAnimeToWatch import displaySelectAnimeToWatchMenu
from lib.MarkCurrentAsComplete import displayMarkCurrentAsCompleteMenu
'''
Main Selection Menu
@author LoganCrockett
'''
def displayMainMenu():
    options = [MenuOption("Add Anime to List", displayAddAnimeToListMenu), MenuOption("Mark Current as Complete", displayMarkCurrentAsCompleteMenu), MenuOption("Select Next to Watch", displaySelectAnimeToWatchMenu)]
    continueLoop = True
    
    while continueLoop:
        try:
            print("What would you like to do ('q' to quit):")
            for i in range(len(options)):
                print(str(i) + ": " + options[i].value)

            userInput = input()

            if userInput == "q" or userInput == "Q":
                continueLoop = False
                break
            
            selectedIndex = int(userInput)

            if selectedIndex < 0 or selectedIndex >= len(options):
                print("Invalid choice. Please select a valid choice\n")
            else:
                options[selectedIndex].onSelect()
        except KeyboardInterrupt:
            continueLoop = False
        except ValueError:
            print("Invalid index value detected")
            continueLoop = False

    print("Exiting program.")

class MenuOption:
    def __init__(self, value, onSelect):
        self.value = value
        self.onSelect = onSelect