def check_sack(content, weight):
    if content not in ['C', 'G', 'S']:
        return f"Error: Invalid content '{content}'"
    if content == 'C' and (weight < 24.9 or weight > 25.1):
        return f"Error: Invalid weight for cement sack '{weight}'"
    if content in ['G', 'S'] and (weight < 49.9 or weight > 50.1):
        return f"Error: Invalid weight for {content} sack '{weight}'"
    return content, weight

def check_order(sacks):
    total_weight = 0
    rejected_sacks = 0
    for sack in sacks:
        result = check_sack(*sack)
        if type(result) == str:
            rejected_sacks += 1
            print(result)
        else:
            total_weight += sack[1]
    return total_weight, rejected_sacks

def calculate_price(sacks):
    prices = {'C': 3, 'G': 2, 'S': 2}
    counts = {'C': 0, 'G': 0, 'S': 0}
    total_price = 0
    for sack in sacks:
        result = check_sack(*sack)
        if type(result) != str:
            counts[sack[0]] += 1
            total_price += prices[sack[0]]
    special_packs = min(counts['C'], counts['G']//2, counts['S']//2)
    discount_price = total_price - special_packs * 2
    return total_price, discount_price, total_price - discount_price
def get_user_input():
    sacks = []
    while True:
        content = input("Enter the content of the sack (C for cement, G for gravel, S for sand): ")
        weight = float(input("Enter the weight of the sack: "))
        sacks.append((content, weight))
        choice = input("Do you want to add another sack? (Y/N): ")
        if choice.upper() != 'Y':
            break
    return sacks

sacks = get_user_input()
total_weight, rejected_sacks = check_order(sacks)
total_price, discount_price, savings = calculate_price(sacks)

print(f"Total weight of the order: {total_weight}")
print(f"Number of rejected sacks: {rejected_sacks}")
print(f"Total price of the order: {total_price}")
print(f"Discounted price of the order: {discount_price}")
print(f"Savings: {savings}")
