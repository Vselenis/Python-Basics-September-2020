num_of_people = int(input())
Back = 0
Chest = 0
Legs = 0
Abs = 0
protein_shake = 0
protein_bar = 0

for person in range(num_of_people):
    activity = input()
    if activity == 'Back':
        Back += 1
    elif activity == 'Chest':
        Chest += 1
    elif activity == 'Legs':
        Legs += 1
    elif activity == 'Abs':
        Abs += 1
    elif activity == 'Protein shake':
        protein_shake += 1
    elif activity == 'Protein bar':
        protein_bar += 1

work = Back + Abs + Legs + Chest
product_buyers = protein_bar + protein_shake

work_procentage = work / num_of_people * 100
product_procentage = product_buyers / num_of_people * 100

print(f"{Back} - back")
print(f"{Chest} - chest")
print(f"{Legs} - legs")
print(f"{Abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_procentage:.2f}% - work out")
print(f"{product_procentage:.2f}% - protein")
