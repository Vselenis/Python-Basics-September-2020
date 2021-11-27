budget = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
number_of_all_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
total_money = number_of_puzzles * 2.60 + number_of_dolls * 3 + number_of_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks * 2
if number_of_all_toys >= 50:
    total_money *= 0.75
total_money *= 0.9
if total_money >= budget:
    print(f'Yes! {(total_money - budget):.2f} lv left.')
else:
    print(f'Not enough money! {(budget-total_money):.2f} lv needed.')
