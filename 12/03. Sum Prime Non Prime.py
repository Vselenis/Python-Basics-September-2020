sum_of_prime_numbers = 0
sum_of_no_prime_numbers = 0
command = input()
while command != 'stop':
    isPrime = True
    number = int(command)
    if number < 0:
        print('Number is negative.')
    else:
        for check in range(2, number):
            if number % check == 0:
                isPrime = False
                break
        if isPrime:
            sum_of_prime_numbers += number
        else:
            sum_of_no_prime_numbers += number
    command = input()
print(f'Sum of all prime numbers is: {sum_of_prime_numbers}')
print(f"Sum of all non prime numbers is: {sum_of_no_prime_numbers}")