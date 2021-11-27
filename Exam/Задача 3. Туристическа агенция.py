import sys

town = input()
pack = input()
vip_disc = input()
days = int(input())

if days <= 0:
    print('Days must be positive number!')
    sys.exit(0)

price_per_day = 0
discount = 0

if town == 'Bansko' or town == 'Borovets':
    if pack == "noEquipment":
        price_per_day = 80
        discount = 0.05
    elif pack == 'withEquipment':
        price_per_day = 100
        discount = 0.10
    else:
        print('Invalid input!')
        sys.exit(0)
elif town == 'Varna' or town == 'Burgas':
    if pack == "noBreakfast":
        price_per_day = 100
        discount = 0.07
    elif pack == 'withBreakfast':
        price_per_day = 130
        discount = 0.12
    else:
        print('Invalid input!')
        sys.exit(0)
else:
    print('Invalid input!')
    sys.exit(0)

if vip_disc == 'yes':
    price_per_day -= price_per_day * discount

if days > 7:
    days -= 1
total = price_per_day * days

print(f'The price is {total:.2f}lv! Have a nice time!')
