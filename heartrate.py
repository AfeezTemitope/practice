firstname = input("enter firstname\n")
lastname = input("enter lastname\n")
middlename = input('enter middleame\n')

month =int(input ('enter month\n'))
day =int(input ('enter day\n'))
years_of_birth = int(input('enter year of birth\n'))

current_year = int(input(" enter current year\n"))

age_in_years = current_year - years_of_birth
maximum_heart_rate = 220 - age_in_years
targeted_heart_rate = maximum_heart_rate * 0.75

print(f'your full name is, {firstname},{lastname}, {middlename}')
print(f'your date of birth is {month}/{day}/{years_of_birth}')
print(f'age in years is {age_in_years}')
print(f'maximum heart rate is {maximum_heart_rate}')
print(f"targeted heart rate is { targeted_heart_rate}")