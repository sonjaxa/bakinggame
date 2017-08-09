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
    "healing slime" : 8,
    "rusty kettle" : 3,
    "powdered fungus" : 6,
    "unicorn horn" : 50,
    "broken wand" : .50,
    "beef jerky" : 3
}

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


thingThing = 2
counterLoop = 2
potionLoopVar = 2
shopLoopVar = 2

bChoice = input("new game ('new') or load previous ('load')?")

if bChoice == "load":
    moneyFile = open("savedMoney.txt", "r")
    lineThing = moneyFile.readline()
    lineThing = lineThing.rstrip("\n")
    moneyFile.close()
    myMoney = int(lineThing)
    # inventory read
    myInventory = {}
    myInventoryFile = open("savedInventory.txt", "r")
    item = myInventoryFile.readline()
    amount = myInventoryFile.readline()
    while item != "":
        item = item.rstrip("\n")
        amount = int(amount.strip("\n"))
        myInventory[item] = amount
        item = myInventoryFile.readline()
        amount = myInventoryFile.readline()
    myInventoryFile.close()


if bChoice == "new":
    myMoney = 300
    myInventory = {
        "broken wand" : 1,
        "beef jerky" : 2,
        "unicorn horn" : 1,
        "tapioca" : 4,
        "powdered fungus" : 4
    }



print("\nYou are on an adventure! Let's make potions!\n")

while thingThing > 0:
    userInputMenu = input("\n'p' to view whats in your pockets\n's' to shop\n'v' to view your money\n'q' to quit\n'c' to mix potion\n'a' to view recipes\n'e' to sell")
    print("\n")

    if userInputMenu == "p":
        print("Currently in pockets:")
        for key, val in myInventory.items():
            print(str(key) + " - " + str(val))
        returnPocketsInput = input("\nenter 'done' to go back to menu!\n")
        if returnPocketsInput == "done":
            continue

    if userInputMenu == "v":
        print(str(myMoney) + "c")
        returnMoneyInput = input("\nenter 'done' to go back to menu!\n")
        if returnMoneyInput == "done":
            continue

    if userInputMenu == "q":
        print("thanks for visiting!")
        thingThing = 0

    if userInputMenu == 'a':
        print("available recipes:\n")
        for key in recipeBook:
            print(key)
        print("\n")
        recipeSearchInput = input("what recipe do you want to look up?")
        print("\n")
        newRecipe = recipeBook[recipeSearchInput]
        print("ingredients needed:\n")
        for key, val in newRecipe.items():
            print(str(val) + " " + str(key))
        returnRecipeInput = input("\nenter 'done' to go back to menu!\n")
        if returnRecipeInput == "done":
            continue

    if userInputMenu == "s":
        print("Welcome to Magicks-R-Us! Mystery tea is on sale!\n")
        for key, val in shopDictionary.items():
            print(str(key) + " - " + str(val))
        print("\nYou have " + str(myMoney) + ("c\n"))
        while counterLoop > 0:
            shopInput = input("Anything strike your fancy, traveler?\n")
            if shopInput == "no":
                print("wow, lame!")
                counterLoop = 0
                break
            countInput = input("How many?\n")
            myMoney = myMoney - shopDictionary[shopInput]*int(countInput)
            deciderShopVar = shopInput in myInventory
            if deciderShopVar == True:
                myInventory[shopInput] = myInventory[shopInput] + int(countInput)
            if deciderShopVar == False:
                myInventory[shopInput] = int(countInput)
            print("you now have " + str(myMoney) + "c\n")
            newShopInput = input("Keep shopping? ")
            if newShopInput == "yes":
                continue
            if newShopInput == "no":
                print("thanks for shopping!")
                counterLoop = 0

    if userInputMenu == "c":
        potionLoopVar = 2
        print("time to brew! available recipes: ")
        for key in recipeBook:
            print(key)
        while potionLoopVar > 0:
            recipeInput = input("what would you like to bake?\n")
            whichRecipe = recipeBook[recipeInput]
            print("items needed for recipe: \n")
            for key, val in whichRecipe.items():
                print (str(val) + " " + str(key))

            potionInput = input("warning: potions cannot be unbrewed. time travel not advised. continue?")

            if potionInput == "yes":
                newVar = 0
                for key in whichRecipe:
                    inventoryAnswer = key in myInventory
                    newVar = newVar + inventoryAnswer
                if newVar > 0:
                    print("insufficient inventory!")
                    newSnackInput = input("try a different potion?")
                    if newSnackInput == "yes":
                        continue
                    if newSnackInput == "no":
                        potionLoopVar = 0
                        break
                for key in whichRecipe:
                    del myInventory[key]
                potionLoopVar = 0
                myInventory[recipeInput] = 1
                print("successful brewing! you now have + 1 " + str(recipeInput) + " in your inventory")

            if potionInput == "no":
                potionLoopVar = 0

    if userInputMenu == 'e':
        while shopLoopVar > 0:
            print("you have available to sell:\n")
            for key, val in myInventory.items():
                print(str(val) + " " + key)
            print("\n")
            sellInput = input("what would you like to sell? ")
            itemSellingPrice = shopDictionary[sellInput]
            qInput = int(input("how many? "))
            qSelling = itemSellingPrice*qInput
            myMoney = myMoney - qSelling
            myInventory[sellInput] = myInventory[sellInput] - qInput
            if myInventory[sellInput] == 0:
                del myInventory[sellInput]
            print("you now have " + str(myMoney) + "c!\n")
            loopInput = input("sell again? ")
            if loopInput == "yes":
                continue
            if loopInput == "no":
                shopLoopVar = 0

# FILE I/O &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

savedMoney = open("savedMoney.txt", "w")
savedMoney.write(str(myMoney))
savedMoney.close()

importedInventory = open("savedInventory.txt", "w")
for key, val in myInventory.items():
    importedInventory.write(key + "\n")
    importedInventory.write(str(val) + "\n")
importedInventory.close()
