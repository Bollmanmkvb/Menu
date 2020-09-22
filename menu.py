from day import *
from datetime import *
from enums import *
from meal import *

class Menu:
    def __init__(self, configPath, boarders):
        menuConfig = configparser.ConfigParser()
        menuConfig.read(configPath)
        self.startDate = datetime.strptime(menuConfig.get("time_period","start"), "%d-%m-%Y")
        self.duration = int(menuConfig.get("time_period","duration")) # in days
        self.days = []
        self.resources = {}
        self.boarders = boarders
        self.secondDinner = menuConfig.get("options","secondDinner")
        self.dinnerLunch = menuConfig.get("options","dinnerLunch")

    # Method creates and fill array of days.
    # Every day has its meals based od given categorizedMeals array.
    def createMenu(self, cathegorizedMeals):
        extendedCategorizedMeals = Meal.extendCategorizedMeals(cathegorizedMeals, self.duration)

        for i in range(0, self.duration):

            if self.secondDinner == "True" :
                currentDay = Day(self.startDate + timedelta(days=i),
                             extendedCategorizedMeals[BREAKFAST][i],
                             extendedCategorizedMeals[MORNINGSNACK][i],
                             extendedCategorizedMeals[LUNCH][i],
                             extendedCategorizedMeals[AFTERNOONSNACK][i],
                             extendedCategorizedMeals[FIRSTDINNER][i],
                             extendedCategorizedMeals[SECONDDINNER][i], )
            else:
                currentDay = Day(self.startDate + timedelta(days=i),
                                 extendedCategorizedMeals[BREAKFAST][i],
                                 extendedCategorizedMeals[MORNINGSNACK][i],
                                 extendedCategorizedMeals[LUNCH][i],
                                 extendedCategorizedMeals[AFTERNOONSNACK][i],
                                 extendedCategorizedMeals[FIRSTDINNER][i], )

            self.days.append(currentDay)

        if self.dinnerLunch == "True":
            for i in range(0, len(self.days)-1):
                self.copyMeal(i, FIRSTDINNER, i+1, LUNCH)

    def printMenu(self):
        for day in self.days:
            Day.printDay(day)

    # Method counts amount of needed resources for created menu.
    def countResources(self):
        boardersCoeficient = 0.0
        for boarder in self.boarders:
            boardersCoeficient += float(boarder.consumptionRatio)

        for day in self.days:
           for meal in day.meals :
               for i in range(0, meal.numberOfParts):
                   if meal.parts[i] in self.resources.keys():
                       self.resources[meal.parts[i]] += boardersCoeficient * int(meal.weightOfParts[i])
                   else:
                       self.resources[meal.parts[i]] = boardersCoeficient * int(meal.weightOfParts[i])

        self.resources = dict(sorted(self.resources.items()))

    def printResources(self):
        for rescource in self.resources:
            print("%s : %d" %(rescource, self.resources[rescource]))

    # Method swap two meals (meal X at day X and meal Y at day Y)in created menu.
    # Indexes start at 0.
    # Method doesn't check if the meals are the same type.
    # Method doesn't check if the indexes are out of range.
    def swapMeals(self, dayX, mealX, dayY, mealY):
        print("swapMeals()...")

    # Method copy attributes of one meal to another (meal X at day X and meal Y at day Y) in created menu.
    # After this method usage the meal Y will have the same attributes as meal X. Meal X remains the same.
    # Indexes start at 0.
    # Method doesn't check if the meals are the same type (meal Y is simply replaced).
    # Method doesn't check if the indexes are out of range.
    def copyMeal(self, dayX, mealX, dayY, mealY):
        self.days[dayY].meals[mealY].name = self.days[dayX].meals[mealX].name
        self.days[dayY].meals[mealY].type = self.days[dayX].meals[mealX].type
        self.days[dayY].meals[mealY].numberOfParts = self.days[dayX].meals[mealX].numberOfParts
        self.days[dayY].meals[mealY].parts = self.days[dayX].meals[mealX].parts.copy()
        self.days[dayY].meals[mealY].weightOfParts = self.days[dayX].meals[mealX].weightOfParts


