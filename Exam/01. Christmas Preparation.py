number_of_paper = int(input())
number_of_plat = int(input())
glue = float(input())
discount = int(input())
disc = discount / 100
price_of_paper = 5.80
price_of_plat = 7.20
price_of_glue = 1.20
total = number_of_paper * price_of_paper + number_of_plat * price_of_plat + glue * price_of_glue
total_price = total - total * disc
print(f'{total_price:.3f}')