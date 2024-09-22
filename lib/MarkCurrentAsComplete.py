from lib.AnimeRecord import AnimeRecord
'''
Displays the Mark Current As Complete Menu
'''
def displayMarkCurrentAsCompleteMenu():
    if len(AnimeRecord.currentWatch) > 0:
            AnimeRecord.markCurrentAsComplete()

            print(AnimeRecord.watched[len(AnimeRecord.watched) - 1] + " is marked as complete.\n")
    else:
        print("Nothing is currently being watched. Please select a new anime to watch\n")