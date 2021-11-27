import math
days_missing = int(input())
all_food = int(input())
first_deer = float(input())
second_deer = float(input())
third_deer = float(input())
total = days_missing * first_deer + days_missing * second_deer + days_missing * third_deer
food_after = all_food - total
if total < all_food:
    print(f'{math.floor(food_after)} kilos of food left.')
else:
    print(f'{abs(math.floor(food_after))} more kilos of food are needed.')