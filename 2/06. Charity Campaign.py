days = int(input())
confectioner = input()
cakes_qunatity = int(input())
waffles_qunatity = int(input())
pancakes_qunatity = int(input())
cakes_price = 45
waffles_price = 5.80
pancakes_price = 3.20
cakes = cakes_price * cakes_qunatity
waffles = waffles_price * waffles_qunatity
pancakes = pancakes_qunatity * pancakes_price
total_days = (cakes +waffles + pancakes) * days
total_camp = total_days * confectioner
total = total_camp - total_camp / 8
print(f'{total} lv')