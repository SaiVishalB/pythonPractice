n = int(input('Enter a number to calculate the sum of digits : '))
b = 0
while n != 0:
    m = n%10
    b += m
    n = n//10
print(b)
