strawberries_price = float(input())
bananas_quantity = float(input())
oranges_qunatity = float(input())
raspberri_quantity = float(input())
strawberries_quantity = float(input())
raspberri_price = strawberries_price / 2
oranges_price = raspberri_price - raspberri_price * 0.4
bananas_price = raspberri_price - raspberri_price * 0.8
needed_money = strawberries_price * strawberries_quantity + bananas_price * bananas_quantity + oranges_price * oranges_qunatity + raspberri_price * raspberri_quantity
print(needed_money)