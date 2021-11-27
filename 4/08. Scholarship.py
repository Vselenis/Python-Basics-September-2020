income = float(input())
grade = float(input())
min_salary = float(input())
social_scholarship = int(min_salary * 0.35)
excelent_scholasrship = int(grade * 25)
if grade >= 5.50:
    if income < min_salary:
        if excelent_scholasrship >= social_scholarship:
            print(f'You get a scholarship for excellent results {excelent_scholasrship} BGN')
        else:
            print(f'You get a Social scholarship {social_scholarship} BGN')
    else:
        print(f'You get a scholarship for excellent results {excelent_scholasrship} BGN')
elif grade > 4.50:
    if income < min_salary:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    else:
        print(f'You cannot get a scholarship!')
else:
    print(f'You cannot get a scholarship!')
