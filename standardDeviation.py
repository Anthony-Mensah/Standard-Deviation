import math

#Recieving numbers in array
n = int(input('How many numbers will you input: '))
numbers = []

for i in range(n):
    number = int(input('Input number: '))
    numbers.append(number)

#Work out the mean of the numbers
def mean():
    sum = 0
    for i in range(n):
        sum = sum + numbers[i]
    return sum / n

#Work out the standard deviation of the numbers
def standardDev():
    sum = 0
    for i in range(n):
        difResult = pow(numbers[i] - mean(), 2)
        sum = sum + difResult

    return math.sqrt(sum / n)

#Final output function
def output():
    print('Standard deviation is {}'.format(standardDev()))

#Output
mean()
standardDev()
output()
