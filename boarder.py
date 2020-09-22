import configparser

class Boarder:
    def __init__(self, name, consumptionRatio):
        self.name = name
        self.consumptionRatio = consumptionRatio

    def printBoarder(self):
        print("    boarderName = " + self.name)
        print("boarderConRatio = " + str(self.consumptionRatio) + "\n")

    @staticmethod
    def printBoarders(boarders):
        for boarder in boarders:
            boarder.printBoarder()

    # Method reads boarders from their config file and return array of Boarder +objects
    # Method expects precise syntax of the config file
    @staticmethod
    def readBoardersFromConfig(configPath):
        boarders = []
        boardersConfig = configparser.ConfigParser()
        boardersConfig.read(configPath)

        for section in boardersConfig.sections():
            currentBoarder = Boarder(boardersConfig.get(section, "name"), boardersConfig.get(section, "ratio"))
            boarders.append(currentBoarder)

        return boarders