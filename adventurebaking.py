# recipes &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
glitterslimeRecipe = {
    "tapioca" : 4,
    "powdered fungus" : 2,
    "unicorn horn" : 1
}

sleepingPowderRecipe = {
    "chamomile root" : 3,
    "enchanted bark" : 1,
    "tylenol pm" : 1
}

lethalSnackRecipe = {
    "belladonna" : 1,
    "dark forest sap": 2,
    "skittles" : 2
}

recipeBook = {
    "healing slime" : glitterslimeRecipe,
    "sleeping powder" : sleepingPowderRecipe,
    "a lethal snack" : lethalSnackRecipe
}

# shop &&&&&&&&&&&&&&&&&&&&&&&&&&&&

shopDictionary = {
    "belladonna" : 25,
    "dark forest sap": 8,
    "skittles" : 1.29,
    "toad + familiar starter kit" : 19.99,
    "chamomile root" : 3,
    "mystery tea" : 2.99,
    "old dirt" : 1,
    "enchanted bark" : 6,
    "tylenol pm" : 4,
    "baby (elf) asprin": 5,
    "dwarfen pottery" : 15,
    "tapioca" : 2,
    "rusty kettle" : 3,
    "powdered fungus" : 6,
    "unicorn horn" : 50
}

# inventory &&&&&&&&&&&&&&&&&&&&&&&&&&

myInventory = {
    "broken wand" : 1,
    "beef jerky" : 2,
    "unicorn horn" : 1
}


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


myMoney = 300
thingThing = 2
counterLoop = 2

print("\nYou are on an adventure in Girlswhocodia! Let's make potions!\n")

while thingThing > 0:
    userInputMenu = input("\n'p' to view whats in your pockets\n's' to shop\n'v' to view your money\n'q' to quit\n'c' to mix potion")
    print("\n")

    if userInputMenu == "p":
        print("Currently in pockets:")
        for key, val in myInventory.items():
            print(str(key) + " - " + str(val))

    if userInputMenu == "v":
        print(str(myMoney) + "c")

    if userInputMenu == "q":
        thingThing = 0

    if userInputMenu == "s":
        print("Welcome to the the Dusty Pantry! Mystery tea is on sale!\n")
        for key, val in shopDictionary.items():
            print(str(key) + " - " + str(val))
        print("\nYou have " + str(myMoney) + ("c\n"))
        while counterLoop > 0:
            shopInput = input("Anything strike your fancy, traveler?\n")
            countInput = input("How many?\n")
            myMoney = myMoney - shopDictionary[shopInput]*int(countInput)
            myInventory[shopInput] = countInput
            print("you now have " + str(myMoney) + "c\n")
            newShopInput = input("Keep shopping? ")
            if newShopInput == "yes":
                continue
            if newShopInput == "no":
                counterLoop = 0

    if userInputMenu == "c":
        print("time to brew! available recipes: ")
        for key in recipeBook:
            print(key)
        recipeInput = input("what would you like to bake?\n")
        thisweirdthing = recipeBook[recipeInput]
        print("items needed for recipe: \n")
        for key, val in thisweirdthing.items():
            print (str(val) + " " + str(key))
