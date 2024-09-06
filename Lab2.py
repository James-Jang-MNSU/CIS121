'''
James Jang
09/06/2024

This program calculates a human age given by the user to animal age on the planet Pythoid
'''

# Reads human age from command prompt
user_human_age = float(input('Enter human age(years): '))

#Dog year calculation - 1 year in human age is 7 years in dog age.
dog_age = user_human_age * 7
dog_age_years = dog_age // 1
dog_age_months = (dog_age - dog_age_years) * 360 // 30
dog_age_days = (dog_age * 360 - dog_age_years * 360 - dog_age_months * 30) // 1
print(f'Your age in dog years is {dog_age_years} years {dog_age_months} months {dog_age_days} days')


#Cat year calculation - 9 years in human age is 1 year in cat age.
cat_age = user_human_age / 9
cat_age_years = cat_age // 1
cat_age_months = (cat_age - cat_age_years) * 12 // 1
cat_age_days = (cat_age * 360 - cat_age_years * 360 - cat_age_months * 30) // 1
print(f'Your age in cat years is {cat_age_years} years {cat_age_months} months {cat_age_days} days')


#Horse year calculation - formula for horse age is 3((human age)^2 - 47)
horse_age = ((user_human_age ** 2 - 47) / 7 + 12) * 3
horse_age_years = horse_age // 1
horse_age_months = (horse_age - horse_age_years) * 360 // 30
horse_age_days = (horse_age * 360 - horse_age_years * 360 - horse_age_months * 30) // 1
print(f'Your age in dog years is {horse_age_years} years {horse_age_months} months {horse_age_days} days')



