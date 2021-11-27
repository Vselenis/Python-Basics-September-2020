budget = float(input())
season = input()
diff = 0
if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        diff = budget * 0.30
        print(f'Camp - {diff:.2f}')
    elif season == 'winter':
        diff = budget * 0.70
        print(f'Hotel - {diff:.2f}')
elif 100 < budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        diff = budget * 0.40
        print(f'Camp - {diff:.2f}')
    elif season == 'winter':
        diff = budget * 0.80
        print(f'Hotel - {diff:.2f}')
elif budget > 1000:
    print('Somewhere in Europe')
    if season == 'summer' or season == 'winter':
        diff = budget * 0.90
        print(f'Hotel - {diff:.2f}')