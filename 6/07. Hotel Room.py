month = input()
nights = float(input())
studio = 0
apartament = 0

if month == 'May' or month == 'October':
    if nights <= 7:
        apartament = 65
        studio = 50
    elif 7 < nights <= 14:
        apartament = 65
        studio = 50 * 0.95
    elif nights > 14:
        apartament = 65 * 0.90
        studio = 50 * 0.70
elif month == 'June' or month == 'September':
    if nights <= 14:
        apartament = 68.70
        studio = 75.20
    elif nights > 14:
        apartament = 68.70 * 0.90
        studio = 75.20 * 0.80
elif month == 'July' or month == 'August':
    if nights <= 14:
        apartament = 77
        studio = 76
    elif nights > 14:
        apartament = 77 * 0.90
        studio = 76
print(f"Apartment: {nights * apartament:.2f} lv.")
print(f'Studio: {nights * studio:.2f} lv.')
