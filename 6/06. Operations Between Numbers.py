one = int(input())
two = int(input())
operator = input()
result = 0

if operator == '+':
    result = one + two
    if result % 2 == 0:
        print(f"{one} {operator} {two} = {result} - even")
    else:
        print(f"{one} {operator} {two} = {result} - odd")
if operator == '-':
    result = one - two
    if result % 2 == 0:
        print(f"{one} {operator} {two} = {result} - even")
    else:
        print(f"{one} {operator} {two} = {result} - odd")
if operator == '*':
    result = one * two
    if result % 2 == 0:
        print(f"{one} {operator} {two} = {result} - even")
    else:
        print(f"{one} {operator} {two} = {result} - odd")
if operator == '/':
    if two == 0:
        print(f'Cannot divide {one} by zero')
    else:
        result = one / two
        print(f'{one} / {two} = {result:.2f}')
elif operator == '%':
    if two == 0:
        print(f'Cannot divide {one} by zero')
    else:
        result = one % two
        print(f'{one} % {two} = {result}')
