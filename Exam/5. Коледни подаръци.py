christmas = input()
kids = 0
adults = 0
toys = 0
sweaters = 0

while christmas != 'Christmas':
    age = int(christmas)
    if age <= 16:
        kids += 1
        toys = kids * 5
    if age > 16:
        adults += 1
        sweaters = adults * 15

    christmas = input()

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys}")
print(f"Money for sweaters: {sweaters}")
