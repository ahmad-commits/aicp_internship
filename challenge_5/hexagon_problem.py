cnic = "XY30155253"


def calcArea(id):
    s = int(id[-1])
    area = 1.5 * 1.732 * s
    return area


def calcPeri(id):
    s = int(id[-1])
    perimeter = 6 * s
    return perimeter


def calcAngleSum():
    a = 120
    sum = 0
    for _ in range(6):
        sum += a
    return sum


def calcAreaSquare(id):
    s = int(id[-1]) + 1
    return s * s


def calcPeriSquare(id):
    s = int(id[-1]) + 1
    return 4 * s


def display(id, shape):
    match shape:
        case "hexagon":
            print("Area of hexagon is:", calcArea(id))
            print("Perimeter of hexagon is:", calcPeri(id))
            print("Sum of angles of hexagon is:", calcAngleSum())
        case "square":
            print("Area of square is:", calcAreaSquare(id))
            print("Perimeter of square is:", calcPeriSquare(id))
        case _:
            return 0


def main():
    print("My CNIC is", cnic)
    print("Enter 1 to calculate area, perimeter, and sum of angles of hexagon")
    print("Enter 2 to calculate area and perimeter of square")
    print("Press any other key to exit")
    userInput = input("")
    match userInput:
        case "1":
            display(cnic, "hexagon")
            main()
        case "2":
            display(cnic, "square")
            main()
        case _:
            exit()


main()
