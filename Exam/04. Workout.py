days_training = int(input())
km_first_day = int(input())
progress = int(input())

total = km_first_day + km_first_day * progress / 100
total_plus = 0
days = 0
while days_training < 1000:
    progress = int(input())
    total_plus = total + total * progress / 100
    days += total_plus
    print(days)