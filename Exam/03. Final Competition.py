number_of_dancers = int(input())
total_score = float(input())
season = input()
place = input()
reward = 0
gift = 0
money = 0
money_per_dancer = 0

if place == 'Bulgaria':
    reward = number_of_dancers * total_score
    if season == 'summer':
        reward *= 0.95
        gift = reward * 0.75
        money = reward - gift
        money_per_dancer = money / number_of_dancers
    elif season == 'winter':
        reward *= 0.92
        gift = reward * 0.75
        money = reward - gift
        money_per_dancer = money / number_of_dancers
elif place == 'Abroad':
    reward = number_of_dancers * total_score
    reward *= 1.5
    if season == 'summer':
        reward *= 0.9
        gift = reward * 0.75
        money = reward - gift
        money_per_dancer = money / number_of_dancers
    elif season == 'winter':
        reward *= 0.85
        gift = reward * 0.75
        money = reward - gift
        money_per_dancer = money / number_of_dancers

print(f"Charity - {gift:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")