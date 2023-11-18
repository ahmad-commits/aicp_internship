student_id = "XY12345678"
source_data = [[55, 65, 75], [120, 150, 170], [210, 230, 240]]


def costSlab1(units):
    return units*10


def costSlab2(units):
    return units*15


def costSlab3(units):
    return units*20


while True:
    print(f"My Student ID is {student_id}")
    print("Enter your choice")
    user_input = input('''Press 1 to display the bill of Slab 1 and Slab 2
Press 2 to display the bill of slab 3
Press any other key to exit.\n''')
    match user_input:
        case '1':
            print("Bill for Slab 1 is")
            for unit in source_data[0]:
                print(costSlab1(unit), end='\t')
            print()
            print("Bill for Slab 2 is")
            for unit in source_data[1]:
                print(costSlab2(unit), end='\t')
            print()
        case '2':
            print("Bill for Slap 3 is")
            for unit in source_data[2]:
                print(costSlab3(unit), end='\t')
            print()
        case _:
            break
