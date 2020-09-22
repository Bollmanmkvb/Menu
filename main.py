import random
from boarder import *
from menu import *

if __name__ == "__main__":

    boarders = Boarder.readBoardersFromConfig("boarders.conf") # read boarders from their config file
    meals = Meal.readMealsFromConfig("meals.conf") # read meals from their config file
    categorizedMeals = Meal.makeCategories(meals) # sort meals to cathegories by type (lunches, dinners...)

    for mealsByType in categorizedMeals :
        mealsByType = random.shuffle(mealsByType) # randomize order of meals in their cathegories

    menu = Menu("menu.conf", boarders) # create menu template for the time period set in days config
    menu.createMenu(categorizedMeals) # fill the menu with meals
    menu.countResources() # count amount of needed rescources for the menu and boarders

    menu.printMenu()
    menu.printResources()