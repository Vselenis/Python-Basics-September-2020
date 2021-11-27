import math

skorost = float(input())
litri = float(input())
total_raztoqnie = 768800
time_needed = math.ceil(total_raztoqnie / skorost)
total_time = time_needed + 3
gorivo = (litri * 768800) / 100
print(total_time)
print(f'{gorivo:.0f}')