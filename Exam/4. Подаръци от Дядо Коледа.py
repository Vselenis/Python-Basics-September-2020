N = int(input())
M = int(input())
S = int(input())

numbers = 0

for numbers in range(M, N+1, -1):
    if numbers % 2 == 0 and numbers % 3 == 0:
        if numbers != S:
            print(f'{numbers}', end= ' ')
        elif numbers == S:
            print(f'{numbers}', end=' ')
            break