target_day = int(input())
money = 0

while target_day != 'closed':
    service = input()
    if service == 'haircut':
        gender = input()
        if gender == 'mens':
            money += 15
        elif gender == 'ladies':
            money += 20
        elif gender == 'kids':
            money += 10
    elif service == 'color':
        paint = input()
        if paint == 'touch up':
            money += 20
        elif paint == 'full color':
            money += 30



        if money >= target_day:
            print("You have reached your target for the day!" )
            break
        elif money < target_day:
            print(f"Target not reached! You need {target_day - money}lv. more.")

        print(f'Earned money: {money}lv.')