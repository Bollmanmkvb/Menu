import configparser

class Meal:
    def __init__(self, name):
        self.name = name.replace("_"," ")
        self.type = []
        self.numberOfParts = 0
        self.parts = []
        self.weightOfParts = []

    def printMeal(self):
        print("     mealName = " + self.name)
        print("     mealtype = " + ", ".join(self.type))
        print("numberOfParts = " + str(self.numberOfParts))
        print("    mealParts = " + ", ".join(self.parts))
        print("weightOfParts = " + ", ".join(self.weightOfParts) + "\n")

    def printMealBrief(self):
        print("     mealName = " + self.name)

    @staticmethod
    def emptyMeal():
        emptyMeal = Meal("Empty")
        emptyMeal.type.append("Empty")
        return  emptyMeal

    @staticmethod
    def printmeals(meals):
        for meal in meals:
            meal.printMeal()

    # Method reads meals from their config file and return array of Meal objects
    # Method expects precise syntax of the config file
    @staticmethod
    def readMealsFromConfig(configPath):
        meals = []
        mealsConfig = configparser.ConfigParser()
        mealsConfig.read(configPath)

        for section in mealsConfig.sections():
            currentMeal = Meal(mealsConfig.get(section, "name"))
            currentMeal.type = mealsConfig.get(section, "type").split("_")

            partindex=0
            partsBeforeParsing =[]
            while mealsConfig.has_option(section, "part_" + str(partindex)):
                partsBeforeParsing.append(mealsConfig.get(section, "part_" + str(partindex)))
                partindex +=1

            for x in partsBeforeParsing:
                weight, part = x.split("-")
                currentMeal.parts.append(part)
                currentMeal.weightOfParts.append(weight)

            currentMeal.numberOfParts = len(partsBeforeParsing)
            meals.append(currentMeal)

        return meals

    # Method takes arry of Meal objects and sort them in arrays bz their cathegories (lunches, dinners...)
    # If one meal fits in more then one cathegory it will be placed in every cathegory, that suits it
    # Method returns array of arrays of Meals objects
    @staticmethod
    def makeCategories(meals):
        cathegorizedMeals = []

        breakfasts = []
        morningSnacks = []
        lunches = []
        afternoonSnacks = []
        firstDinners = []
        secondDinners = []

        for meal in meals:
            if "breakfast" in meal.type :
                breakfasts.append(meal)
            if "morningsnack" in meal.type :
                morningSnacks.append(meal)
            if "lunch" in meal.type :
                lunches.append(meal)
            if "afternoonsnack" in meal.type :
                afternoonSnacks.append(meal)
            if "firstdinner" in meal.type :
                firstDinners.append(meal)
            if "seconddinner" in meal.type :
                secondDinners.append(meal)

        cathegorizedMeals.append(breakfasts)
        cathegorizedMeals.append(morningSnacks)
        cathegorizedMeals.append(lunches)
        cathegorizedMeals.append(afternoonSnacks)
        cathegorizedMeals.append(firstDinners)
        cathegorizedMeals.append(secondDinners)

        return cathegorizedMeals

    # Method extends given array of Meal objects
    # For example: If given array of Meal object has length 3 and desired duration is 6 days,
    #              the method will append the same array
    #              given array = [1, 2, 3]
    #              extended array = [1, 2, 3, 1, 2, 3]
    @staticmethod
    def extendMeals(meals, duration):
        originalLenght = len(meals)
        while len(meals) < duration:
            meals.append(meals[ len(meals) - originalLenght ]) # cyclic append arrays (sliding window system)

    # Method extends all meal cathegories regarding the desired duration
    @staticmethod
    def extendCategorizedMeals(categorizedMeals, duration):
        extendedCategorizedMeals = categorizedMeals

        for categorizedMealArray in extendedCategorizedMeals:
            Meal.extendMeals(categorizedMealArray, duration)

        return  extendedCategorizedMeals