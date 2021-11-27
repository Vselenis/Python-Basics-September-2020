month = input()
all_hours = int(input())
all_people = int(input())
unit = input()
price = 0

if month == 'may' or month == 'march' or month == 'april':
    if unit == 'day':
        price = 10.50
    elif unit == 'night':
        price = 8.40
elif month == 'july' or month == 'june' or month == 'august':
    if unit == 'day':
        price = 12.60
    elif unit == 'night':
        price = 10.20

if all_people >= 4:
    price *= 0.9

if all_hours >= 5:
    price *= 0.5

hours = all_people * all_hours
total = price * hours

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total:.2f}")