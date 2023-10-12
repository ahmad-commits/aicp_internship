from os import system,  name
import sys
from time import sleep

days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def check_frequent_parking(parking_number) -> bool:
    integer_digits = len(parking_number)
    if integer_digits == 5:
        check_digit = int(parking_number[-1])
        weighted_sum = 0
        i = integer_digits
        x = 0
        while i > 1:
            weighted_sum += i * int(parking_number[x])
            i -= 1
            x += 1
        return (check_digit == (11 - (weighted_sum % 11))) or (
            check_digit == 0 and (weighted_sum % 11 == 0)
        )
    else:
        return False


day_total = []


def calculate_parking_fair(day, arrival_hour, parking_time, discount_eligibility):
    calculatedFair = 0
    beforeEvening = arrival_hour < 16
    if arrival_hour + parking_time > 24:
        print("Parking time exceeds midnight")
        return -1

    if discount_eligibility:
        print("You are eligible for discount!")
        if arrival_hour >= 16:
            discount_factor = 0.5
        else:
            discount_factor = 0.9
    if day.lower() in days:
        match day:
            case "sunday":
                if parking_time > 8:
                    print("You can't park for more than 8 hours on Sundays")
                    return -1
                if beforeEvening:
                    hourly_rate = 2
            case "saturday":
                if parking_time > 4:
                    print("You can't park for more than 4 hours on Saturdays")
                    return -1
                if beforeEvening:
                    hourly_rate = 3
            case _:
                if parking_time > 2:
                    print("Parking for more than 2 hours isn't available on weekdays")
                    return -1
                hourly_rate = 10
        if not beforeEvening:
            hourly_rate = 2
            calculatedFair = hourly_rate * parking_time
            if discount_eligibility:
                calculatedFair *= discount_factor
            print("Your parking fair is:")
            return calculatedFair
        if arrival_hour >= 0 and arrival_hour <=8:
            print("Parking is not allowed at this time")
            return - 1
        if arrival_hour + parking_time > 16 and arrival_hour < 16:
            calculatedFair += hourly_rate * (16 - arrival_hour)
            print(16 - arrival_hour, "hour(s) before 16:00: ", calculatedFair, "$")
            calculatedFair += 2 * (arrival_hour + parking_time - 16)
            print(
                arrival_hour + parking_time - 16,
                "hour(s) after 16:00: ",
                2 * (arrival_hour + parking_time - 16),
                "$",
            )
            print("Total Amount: ", calculatedFair, "$")
            if discount_eligibility:
                calculatedFair *= discount_factor
                print("After applying discount:", calculatedFair, "$")
            print("Final Amount:")
            return calculatedFair
        else:
            calculatedFair += hourly_rate * parking_time

        if discount_eligibility:
            calculatedFair *= discount_factor
        return calculatedFair
    else:
        print("Weekday name is invalid")


daily_total = 0


def parking_request():
    input_parking_hour = int(input("Entry hour: "))
    input_parking_time = int(input("Parking time in hour(s): "))
    is_frequent_parker = input("Do you have a frequent parking number? (yes/no): ")
    if is_frequent_parker == "yes":
        parker_id = input("Frequent Parking Number: ")
        if not check_frequent_parking(parker_id):
            print("You entered an invalid Frequent Parking Number")
            sleep(2)
            clear()
            parking_request()
        else:
            validity = True
    elif is_frequent_parker == "no":
        validity = False

    query = calculate_parking_fair(
        today, input_parking_hour, input_parking_time, validity
    )
    print(query)
    if query != -1:
        save_prompt = input("Do you want to confirm this ticket (yes/no): ")
        match save_prompt:
            case "yes":
                day_total.append(query)
            case _:
                None
        clear()
        main()


def getTotal():
    print("Total cash collected today: ", sum(day_total))
    sys.exit()


today = input("Day: ")
while not today.lower() in days:
    print("Invalid weekday name entered.")
    today = input("Day: ")


def main():
    print("Parking Lot Management System")
    print("1. Parking Request")
    print("2. End Day")
    print("3. Exit Program")
    selection = input("What do you want to do: ")
    match selection:
        case "1":
            parking_request()
        case "2":
            getTotal()
        case "3":
            sys.exit()
        case _:
            print("Invalid Selection")
            sleep(1)
            clear()

    main()


main()
