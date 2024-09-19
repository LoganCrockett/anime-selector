from lib.AnimeRecord import AnimeRecord
import random
'''
Select Anime to Watch Menu
@author LoganCrockett
'''
def displaySelectAnimeToWatchMenu():
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

    print("Current items up for selection: " + str(toSelectList))
    print("Press enter when you are ready to select")
    input()

    AnimeRecord.setCurrentWatch(random.choice(toSelectList))
    print("Current watch is now: " + AnimeRecord.currentWatch)
    print()
    return
