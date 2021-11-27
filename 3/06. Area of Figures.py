import math
type = input()
if type == 'square':
    a = float(input())
    area_square = math.pow(a, 2)
    print(area_square)
elif type == 'rectangle':
    a = float(input())
    b = float(input())
    area_rectangle = a * b
    print(area_rectangle)
elif type == 'circle':
    r = float(input())
    area_circle = math.pi * math.pow(r, 2)
    print(area_circle)
elif type == 'triangle':
    a = float(input())
    h = float(input())
    area_triangle = a * h / 2
    print(area_triangle)