charities = []
totals = []

for i in range(3):
    charity = input(f"Enter the name of charity {i+1}: ")
    charities.append(charity)
    totals.append(0)

while True:
    for i, charity in enumerate(charities):
        print(f"{i+1}. {charity}")

    choice = int(input("Enter your charity choice (1, 2, 3, or -1 to show totals): "))
    if choice == -1:
        break
    elif choice not in [1, 2, 3]:
        print("Invalid choice. Please enter 1, 2, 3, or -1.")
        continue

    bill = float(input("Enter the value of your shopping bill: "))
    donation = bill * 0.01

    totals[choice-1] += donation

    print(f"Donated ${donation:.2f} to {charities[choice-1]}.")

sorted_charities_and_totals = sorted(zip(charities, totals), key=lambda x: x[1], reverse=True)

grand_total = 0
for charity, total in sorted_charities_and_totals:
    print(f"{charity}: ${total:.2f}")
    grand_total += total

print(f"GRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")