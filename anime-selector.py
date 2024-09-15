from lib.MainMenu import displayMainMenu
from lib.AnimeRecord import AnimeRecord

'''
Program to allow users to add anime to the list, and randomly select anime to watch
@author LoganCrockett
'''
def animeSelector():
    print("Welcome to the anime selector\n")
    AnimeRecord.loadData()
    displayMainMenu()
    AnimeRecord.writeRecordState()

animeSelector()