shop_items = {
    "case": {"A1": ["Compact", 75], "A2": ["Tower", 150]},
    "ram": {"B1":["8GB", 79.99], "B2":["16GB", 149.99], "B3":["32GB", 299.99]},
    "mainHDD": {"C1":["1 TB", 49.99], "C2": ["2 TB", 89.99], "C3": ["4 TB", 129.99]},
    "SSD": {"D1": ["240GB", 59.99], "D2": ["480GB", 119.99]},
    "secondaryHDD": {"E1": ["1 TB", 49.99], "E2": ["2 TB", 89.99], "E3": ["4 TB", 129.99]},
    "opticalDrive": {"F1": ["DVD/Blu-Ray Player", 50], "F2": ["DVD/Blu-Ray Re-Writer", 100]},
    "operatingSystem": {"G1": ["Standard", 100.00], "G2": ["Professional", 175.00]},
}

def listItems(query):
    for q in shop_items[query]:
        for model in shop_items[query][q]:
            print(model, end=" ")
        print("", end="$\n")


listItems("ram")