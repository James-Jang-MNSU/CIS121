'''
9/19/2024
James Jang

This program checks the numbers of abundant, deficient, and perfect 
numbers that are in between 1 and the upper bound given by the user
'''

upper_bound = int(input('Enter an upper bound for a check: '))

num_of_abundants = 0
num_of_deficients = 0
num_of_perfects = 0

for iteration in range(1, upper_bound+1):    
    #proper_divisors = []
    sum_of_divisors = 0
    for num in range(1, iteration):
        if iteration % num == 0:
            #proper_divisors.append(num)
            sum_of_divisors += num
    if sum_of_divisors > iteration:
        num_of_abundants += 1
    elif sum_of_divisors < iteration:
        num_of_deficients += 1
    else:
        num_of_perfects += 1

print('Between 1 and', upper_bound, 'there are')
print(num_of_deficients, 'deficient numbers')
print(num_of_perfects, 'perfect numbers')
print(num_of_abundants, 'abundant numbers')
