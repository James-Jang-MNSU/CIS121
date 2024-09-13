'''
James Jang
9/12/2024

This program reads the user's income and marital status 
and calculates the amount of tax charged for the year 2023
'''

user_income = int(input('Enter the amount of income you earned in 2023: '))
user_marital_status = input('Are you married or single?\nType m for married and s for single: ')
user_tax = 0

if user_marital_status == 's':
	if 0 <= user_income <= 11000:
		user_tax = user_income * 0.10
	if 11001 <= user_income <= 44725:
		user_tax = 11000 * 0.1 + (user_income - 11000) * 0.12
	if 44726 <= user_income <= 95375:
		user_tax = 11000 * 0.1 + 33725 * 0.12 + (user_income - 44725) * 0.22
	if user_income > 95375:
		print('You made too much for this calculator. Hurray!')
		user_tax = 'n/a'
		
elif user_marital_status == 'm':
	if 0 <= user_income <= 22000:
		user_tax = user_income * 0.10
	if 22001 <= user_income <= 89450:
		user_tax = 22000 * 0.1 + (user_income - 22000) * 0.12
	if 89451 <= user_income <= 190750:
		user_tax = 22000 * 0.1 + 67450 * 0.12 + (user_income - 89450) * 0.22
	if user_income > 190750:
		print('You made too much for this calculator. Hurray!')
		user_tax = 'n/a'
else:
	print('Invalid input for marital status')
	
if user_tax != 'n/a':
	print(f'This year you owe {user_tax:.2f} in taxes')

'''
	if 95376 <= user_income <= 182100:
		tax_rate = 0.24
	if 182101 <= user_income <= 231250:
		tax_rate = 0.32
	if 231251 <= user_income <= 578125:
		tax_rate = 0.35
	if 578126 <= user_income:
		tax_rate = 0.37
'''

'''
	if 190751 <= user_income <= 364200:
		tax_rate = 0.24
	if 364201 <= user_income <= 462500:
		tax_rate = 0.32
	if 462501 <= user_income <= 693750:
		tax_rate = 0.35
	if 693751 <= user_income:
		tax_rate = 0.37
'''

