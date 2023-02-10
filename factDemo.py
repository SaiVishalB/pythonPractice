n = int(input('Enter a number to calculate factorial : '))
x = n
for i in range(1,n):
    n = n*i
print('The factorial is ')
print(n)