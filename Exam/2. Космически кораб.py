import math
width_ship = float(input())
length_ship = float(input())
height_ship = float(input())
height_astro = float(input())

volume_sheep = width_ship * length_ship * height_ship
volume_of_room = (height_astro + 0.40) * 2 * 2
total_astro = math.floor(volume_sheep / volume_of_room)

if total_astro < 3:
    print("The spacecraft is too small.")
if 3 < total_astro < 10:
    print(f"The spacecraft holds {total_astro} astronauts.")
if total_astro > 10:
    print("The spacecraft is too big.")