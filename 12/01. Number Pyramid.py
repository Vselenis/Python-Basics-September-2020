number = int(input())
number_print = 1
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(f'{number_print}', end = ' ')
        number_print += 1
        if number_print > number:
            break
    if number_print > number:
        break
    print()
