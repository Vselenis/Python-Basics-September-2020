first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    number_is_string = str(number)
    odd = 0
    even = 0
    for index ,digit in enumerate(number_is_string):
        if index % 2 == 0:
            odd += int(digit)
        else:
            even += int(digit)
    if odd == even:
        print(f'{number_is_string}', end = ' ')