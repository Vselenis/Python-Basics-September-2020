import math
world_record = float(input())
m = float(input())
seconds_m = float(input())
total_seconds = m * seconds_m
add_time = m / 15
down = math.floor(add_time)
add = down * 12.5
total_time = total_seconds + add

if world_record > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f"No, he failed! He was {(total_time - world_record):.2f} seconds slower.")

