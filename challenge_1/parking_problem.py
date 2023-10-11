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


def getParkingFair(day, arrival_hour, parking_time, frequent_parking_number="00100"):
    discount_factor = 0
    discount_eligibility = check_frequent_parking(frequent_parking_number)
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
    else:
        print("Frequent Parking Number is Invalid!")
    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    if day.lower() in days:
        match day:
            case "sunday":
                if beforeEvening:
                    hourly_rate = 2
            case "saturday":
                if beforeEvening:
                    hourly_rate = 3
                else:
                    hourly_rate = 0
            case _:
                hourly_rate = 10
        if not beforeEvening:
            hourly_rate = 2
            calculatedFair = hourly_rate * parking_time
            return calculatedFair
        if arrival_hour + parking_time > 16 and arrival_hour < 16:
            calculatedFair += hourly_rate * (16 - arrival_hour)
            calculatedFair += 2 * (arrival_hour + parking_time - 16)
            return calculatedFair
        else:
            calculatedFair += hourly_rate * parking_time

        if discount_eligibility:
            calculatedFair *= discount_factor

        print("Your parking fair is:")
        return calculatedFair
    else:
        print("Weekday name is invalid")


print(getParkingFair("sunday", 14, 6, "12345"))
print(check_frequent_parking("12345"))
