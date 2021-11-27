import math
import sys
number_of_airlines = int(input())
best_airline = ''
average = 0
max = -sys.maxsize

for air in range(number_of_airlines):
    airline = input()
    total_points = 0
    total_passengers = 0
    passengers = input()

    while passengers != 'Finish':
        total_passengers += int(passengers)
        total_points += 1
        passengers = input()
        average = total_passengers / total_points
    print(f"{airline}: {math.floor(average)} passengers.")
        if average > max:
            max = average
            best_airline = airline
            print(f"{best_airline} has most passengers per flight: {math.floor(average)}")









