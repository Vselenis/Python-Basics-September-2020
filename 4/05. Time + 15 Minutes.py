enter_hour = int(input())
enter_mins = int(input())
time_in_mins = enter_hour * 60 + enter_mins
time_after = time_in_mins + 15
hours_after = time_after // 60
minutes_after = time_after % 60
if hours_after > 23:
    hours_after = 0
if minutes_after < 10:
    print(f'{hours_after}:0{minutes_after}')
else:
    print(f'{hours_after}:{minutes_after}')
