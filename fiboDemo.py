n = int(input('Enter a number to find fibonacci series : '))
a = 0
b = 1
count = 0
print('calculating fibonacci : ')
print(a,"\n",b)
while n-1:
    c = a+b
    a = b
    b = c
    print(b)
    n = n-1
