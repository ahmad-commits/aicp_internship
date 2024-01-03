return_times = [10] * 10
money_taken = [0] * 10
hours_hired = [0] * 10

while True:
    current_time = input("Enter the current time (HH:MM, or -1 to end the day): ")
    if current_time == "-1":
        break

    try:
        hours, minutes = map(int, current_time.split(":"))
        if hours < 10 or hours > 17 or minutes < 0 or minutes > 59:
            print("Invalid time. Please enter a time between 10:00 and 17:59.")
            continue
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format.")
        continue

    available_boats = [i+1 for i, return_time in enumerate(return_times) if return_time <= hours + minutes/60]

    if not available_boats:
        print("No boats available. The next boat will be available at", min(return_times))
        continue

    print("Available boats:", available_boats)
    boat = int(input("Choose a boat to hire: ")) - 1

    duration = float(input("Enter hire duration (0.5 or 1 hour): "))
    if duration != 0.5 and duration != 1:
        print("Invalid duration. Please enter either 0.5 or 1 hour.")
        continue

    cost = 20 if duration == 1 else 12

    return_times[boat] = hours + minutes/60 + duration
    money_taken[boat] += cost
    hours_hired[boat] += duration

total_money = sum(money_taken)
total_hours = sum(hours_hired)

unused_boats = [i+1 for i, hours in enumerate(hours_hired) if hours == 0]
most_used_boat = hours_hired.index(max(hours_hired)) + 1

print("Total money taken:", total_money)
print("Total hours hired:", total_hours)
print("Unused boats:", unused_boats)
print("Most used boat:", most_used_boat)

for boat, money in enumerate(money_taken):
    print(f"Total money taken for boat {boat+1}: {money}")
