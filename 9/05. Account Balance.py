text = input()
balance = 0


while text != "NoMoreMoney":
    diff = float(text)
    if diff < 0:
        print("Invalid operation!")
        break
    elif diff > 0:
        balance += diff
        print(f'Increase: {diff:.2f}')
        text = input()

print(f'Total: {balance:.2f}')