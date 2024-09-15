import json

RECORD_FILE_PATH="assets/animeRecord.json"

'''
Object that will represnt the state is a json file for anime in the following format:
- toWatch
- currentWatch
- watched
@author LoganCrockett
'''
class AnimeRecord:
    toWatch = set()
    currentWatch = ""
    watched = list()

    def __new__():
        pass

    @staticmethod
    def loadData():
        try:
            recordFile = open(RECORD_FILE_PATH, "rt")
            jsonDict = json.loads(recordFile.read())

            AnimeRecord.toWatch = set(jsonDict["toWatch"])
            AnimeRecord.currentWatch = jsonDict["currentWatch"]
            AnimeRecord.watched = jsonDict["watched"]

            recordFile.close()
        except FileNotFoundError:
            ## Do Nothing. File Will be created later
            pass

    '''
    Adds a new anime name to the toWatch set
    '''
    @staticmethod
    def addNewAnimeToWatch(animeName: str):
        formattedName = animeName.lower().title()
        if formattedName not in AnimeRecord.watched:
            AnimeRecord.toWatch.add(formattedName)

    '''
    Marks what is currently being watched as complete
    '''
    @staticmethod
    def markCurrentAsComplete():
        if len(AnimeRecord.currentWatch) > 0:
            AnimeRecord.watched.append(AnimeRecord.currentWatch)
            AnimeRecord.currentWatch = ""

            print(AnimeRecord.watched[len(AnimeRecord.watched) - 1] + " is marked as complete.\n")

    '''
    Writes the state of this class to a json file
    '''
    @staticmethod
    def writeRecordState():
        with open(RECORD_FILE_PATH, "wt") as writeFile:
            writeFile.write(
                json.dumps({
                    "toWatch": list(AnimeRecord.toWatch),
                    "currentWatch": AnimeRecord.currentWatch,
                    "watched": AnimeRecord.watched
                })
            )
