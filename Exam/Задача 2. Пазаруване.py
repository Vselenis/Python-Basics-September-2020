budget = float(input())
number_of_videocards = int(input())
number_of_processor = int(input())
num_of_ram = int(input())

price_of_videocards = number_of_videocards * 250
price_of_processors = number_of_processor * (0.35 * price_of_videocards)
price_of_ram = num_of_ram * (0.10 * price_of_videocards)

total = price_of_videocards + price_of_processors + price_of_ram

if number_of_videocards > number_of_processor:
    total -= total * 0.15

if budget >= total:
    print(f'You have {budget - total:.2f} leva left!')
else:
    print(f'Not enough money! You need {total - budget:.2f} leva more!')