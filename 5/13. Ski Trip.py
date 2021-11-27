days = int(input())
room_type = input()
grade = input()

final_price = 0
nights = days - 1

if room_type == 'room for one person':
    final_price = nights * 18
elif room_type == 'apartament':
    final_price = nights * 25
    if days < 10:
        final_price *= 0.7
    elif 10 <= days <= 15:
        final_price *= 0.65
    else:
        final_price *= 0.5
elif room_type == 'president apartament':
    final_price = nights * 35
    if days < 10:
        final_price *= 0.9
    elif 10 <= days <= 15:
        final_price *= 0.85
    else:
        final_price *= 0.8

if grade == 'positive':
    final_price *= 1.25
elif grade == 'negative':
    final_price *= 0.9

print(f'{final_price:.2f}')
