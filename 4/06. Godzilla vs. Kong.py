budget = float(input())
number_of_statists = int(input())
clothing_price = float(input())
decor = budget * 0.10

if number_of_statists > 150:
    clothing_price *= 0.90
total_price = clothing_price * number_of_statists
total = decor + total_price

if total > budget:
    print('Not enough money!')
    print(f'Wingard needs {total - budget:.2f} leva more.')
elif total <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total:.2f} leva left.")
