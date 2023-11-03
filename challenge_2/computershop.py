inventory = {
    "basic": {"X": ["Basic Components", 200.00]},
    "case": {"A1": ["Compact Case", 75.0], "A2": ["Tower Case", 150.0]},
    "ram": {
        "B1": ["8GB RAM", 79.99],
        "B2": ["16GB RAM", 149.99],
        "B3": ["32GB RAM", 299.99],
    },
    "mainHDD": {
        "C1": ["1 TB HDD", 49.99],
        "C2": ["2 TB HDD", 89.99],
        "C3": ["4 TB HDD", 129.99],
    },
    "SSD": {"D1": ["240GB", 59.99], "D2": ["480GB", 119.99]},
    "secondaryHDD": {
        "E1": ["1 TB", 49.99],
        "E2": ["2 TB", 89.99],
        "E3": ["4 TB", 129.99],
    },
    "opticalDrive": {
        "F1": ["DVD/Blu-Ray Player", 50.00],
        "F2": ["DVD/Blu-Ray Re-Writer", 100.00],
    },
    "operatingSystem": {
        "G1": ["Standard Edition", 100.00],
        "G2": ["Professional Edition", 175.00],
    },
}
width = 50


def listItems(query, title):
    print(f"╭{'─'*width}╮")
    print(f"│{title}{' '*(width-len(title))}│")
    for itemCode in inventory[query]:
        space = len(str(inventory[query][itemCode][0])) + len(
            str(inventory[query][itemCode][1])
        )
        rem = width - space - 6
        print(
            f"├{'─'*(width)}┤\n│{itemCode}┊{' '*((rem)//2)}-{inventory[query][itemCode][0]}-{' '*((rem+1)//2)}{inventory[query][itemCode][1]}$│"
        )
    print(f"╰{'─'*width}╯")


def itemsTable(itemList, heading):
    totalCost = 0
    print(f"╭{'─'*width}╮\n│{heading}{' '*(width-len(heading))}│\n├{'─'*width}┤")
    for item in itemList:
        itemName = inventory[item[0]][item[1]][0]
        itemCost = inventory[item[0]][item[1]][1]
        totalCost += itemCost
        itemCost = str(itemCost)
        print(
            f"│{' '*((1+width-len(itemName)-len(itemCost)-4)//2)}{itemName}:  {itemCost}${' '*((width - len(itemName) -len(itemCost)-4)//2)}│"
        )
    print(f"╰{'─'*(width)}╯\n╭{'─'*width}╮")
    print(f"│Items Cost:{' ' * (width - len(str(totalCost)) - 13)} {totalCost}$│")
    print(f"╰{'─'*width}╯")
    return totalCost


def main():
    orderList = [["basic", "X"]]
    listItems("case", "Choose from these cases")
    wrongItemCode = "Input error. Enter correct item code."

    userCase = input("Enter item code of your desired case: ")
    while userCase not in inventory["case"]:
        print(wrongItemCode)
        userCase = input("Enter item code of your desired case: ")
    print("You chose: ", inventory["case"][userCase][0])
    orderList.append(["case", userCase])
    listItems("ram", "Available RAM")
    userRAM = input("Enter item code of your desired RAM: ")
    while userRAM not in inventory["ram"]:
        print(wrongItemCode)
        userRAM = input("Enter item code of your desired RAM:")
    print("You chose", inventory["ram"][userRAM][0])
    orderList.append(["ram", userRAM])
    listItems("mainHDD", "Available Hard Drives")

    userHDD = input("Enter item code of your desired hard drive: ")
    while userHDD not in inventory["mainHDD"]:
        print(wrongItemCode)
        userHDD = input("Enter item code of your desired hard drive: ")
    print("You chose", inventory["mainHDD"][userHDD][0])
    orderList.append(["mainHDD", userHDD])
    itemsTable(orderList, "You chose these products")
    addlItems = input("Do you want any additional items (yes/no): ")
    if addlItems == "yes":
        addlList = []
        addlRequest = True
        itemsBought = 0
        while addlRequest == True:
            heading = "Additional Items: "
            itemDescription = [
                "Case",
                "RAM",
                "Main Hard Drive",
                "Secondary Hard Drive",
                "Solid State Drive",
                "Optical Drive",
                "Operating System",
            ]
            print(
                f"╭{'─'*width}╮\n│{heading}{' '*(width-len(heading))}│\n├{'─'*width}┤"
            )
            i = 1
            for name in itemDescription:
                spaces = width - len(name) - 2
                print(f"│{i}.{' '*((1+spaces)//2)}{name}{' '*(spaces//2)}│")
                print(f"│{'─'*width}│")
                i += 1
            print(f"╰{'─'*(width)}╯")
            categoryNumber = input("Enter item number: ")
            while not categoryNumber in ["1", "2", "3", "4", "5", "6", "7"]:
                print("Error. Enter Correct Item Number from List")
                categoryNumber = input("Enter item number: ")
            match categoryNumber:
                case "1":
                    item = "Case"
                    itemCategory = "case"
                    listItems(itemCategory, item)
                case "2":
                    item = "RAM"
                    itemCategory = "ram"
                    listItems(itemCategory, item)
                case "3":
                    item = "Main Hard Disk"
                    itemCategory = "mainHDD"
                    listItems(itemCategory, item)
                case "4":
                    item = "Secondary Hard Disk"
                    itemCategory = "secondaryHDD"
                    listItems(itemCategory, item)
                case "5":
                    item = "Solid State Drive"
                    itemCategory = "SSD"
                    listItems(itemCategory, item)
                case "6":
                    item = "Optical Drive"
                    itemCategory = "opticalDrive"
                    listItems(itemCategory, item)
                case "7":
                    item = "Operating System"
                    itemCategory = "operatingSystem"
                    listItems(itemCategory, item)
                case _:
                    print("Error")
            choice = input(f"Enter item code of your desired {item}: ")
            while choice not in inventory[itemCategory]:
                print(wrongItemCode)
                choice = input(f"Enter item code of your desired {item}: ")
            confirmItem = input(f"Add {choice} to your order? (yes/no): ")
            while confirmItem not in ["yes", "no"]:
                print("Enter yes or no")
                confirmItem = input(f"Add {choice} to your order? (yes/no): ")
            if confirmItem == "no":
                continue
            else:
                addlList.append([itemCategory, choice])
                itemsBought += 1
                print("Item added to your order")
            continueAddl = input("Do you want any more additional items (yes/no):")
            while continueAddl not in ["yes", "no"]:
                print("Enter yes or no")
                continueAddl = input("Do you want any more additional items (yes/no):")

            if continueAddl == "no":
                addlRequest = False
        totalCost = 0
        totalCost += itemsTable(orderList, "Main Order")
        totalCost += itemsTable(addlList, "Additional Items")
        if itemsBought >= 1:
            if itemsBought > 1:
                print(f"You are eligible for 10% discount!")
                discountedPrice = 0.9 * totalCost
            else:
                print(f"You are eligible for 5% discount!")
                discountedPrice = 0.95 * totalCost

            discountedPrice = round(discountedPrice, 2)
            amountSaved = round(totalCost - discountedPrice, 2)
            print(f"╭{'─'*width}╮")
            print(f"│Total Cost:{' '*(width - len(str(totalCost)) - 12)}{totalCost}$│")

            print(
                f"│Discounted Price: {' '*(width - len(str(discountedPrice)) - 19)}{discountedPrice}$│"
            )
            print(
                f"│You save: {' '*(width - len(str(amountSaved)) - 11)}{amountSaved}$│"
            )
            print(f"╰{'─'*width}╯")
    else:
        totalCost = 0
        totalCost += itemsTable(orderList, "Main Order")
        totalCost = str(totalCost)
        print(f"╭{'─'*width}╮")
        print(f"│Total Cost:{' '*(width - len(totalCost) - 12)}{totalCost}$│")
        print(f"╰{'─'*width}╯")

    confirmOrder = input("Are you satisfied with this order (yes/no): ")
    while confirmOrder not in ["yes", "no"]:
        print("Enter yes or no")
        confirmOrder = input("Are you satisfied with this order (yes/no): ")

    if confirmOrder == "yes":
        print("Thank you for your purchase!. We expect you to come again")
    else:
        restartOrder = input("Do you want to start from beginning (yes/no): ")
        while restartOrder not in ["yes", "no"]:
            print("Enter yes or no")
            restartOrder = input("Do you want to start from beginning (yes/no): ")
        if restartOrder == "yes":
            main()
        else:
            print("We regret to see you go.")


main()
