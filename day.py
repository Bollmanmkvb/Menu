from enums import *
from meal import *

class Day:
    def __init__(self, date, breakfast, morningSnack, lunch, afternoonSnack, firstDinner, secondDinner=Meal.emptyMeal()):
        self.date = date
        self.meals = [breakfast, morningSnack, lunch, afternoonSnack, firstDinner, secondDinner]

    def printDay(self):
        print("Date = " + self.date.strftime("%d. %m. %Y"))

        print("Brekafast")
        Meal.printMealBrief(self.meals[BREAKFAST])
        print("Morningsnack")
        Meal.printMealBrief(self.meals[MORNINGSNACK])
        print("Lunch")
        Meal.printMealBrief(self.meals[LUNCH])
        print("Afternoonsnack")
        Meal.printMealBrief(self.meals[AFTERNOONSNACK])
        print("First Dinner")
        Meal.printMealBrief(self.meals[FIRSTDINNER])

        if self.meals[SECONDDINNER].type[0] != "Empty":
            print("Second Dinner")
            Meal.printMealBrief(self.meals[SECONDDINNER])

        print("\n")