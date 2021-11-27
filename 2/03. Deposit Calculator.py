deposit = float(input())
months = int(input())
interest = float(input())
monthly_interest = deposit * interest / 100 / 12
total_money = deposit + months * monthly_interest
print(total_money)
