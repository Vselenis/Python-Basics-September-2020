flowers = input()
quantity_of_flowers = int(input())
budget = int(input())
price = 0
total = 0

if flowers == 'Roses':
    price = 5
    if quantity_of_flowers > 80:
        price *= 0.9
elif flowers == 'Dahlias':
    price = 3.80
    if quantity_of_flowers > 90:
        price *= 0.85
elif flowers == 'Tulips':
    price = 2.80
    if quantity_of_flowers > 80:
        price *= 0.85
elif flowers == 'Narcissus':
    price = 3
    if quantity_of_flowers < 120:
        price *= 1.15
elif flowers == 'Gladiolus':
    price = 2.5
    if quantity_of_flowers < 80:
        price *= 1.20
total = quantity_of_flowers * price
difference = abs(budget - total)
if budget >= total:
    print(f'Hey, you have a great garden with {quantity_of_flowers} {flowers} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
