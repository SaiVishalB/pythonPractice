n = int(input('Enter a number to evaluate armstrong: '))
sum = 0
d = n
while n!=0:
    temp = n%10
    sum += temp**3
    n = n//10
if(d==sum):
    print(d,' is armstrong')
else:
    print(d,' is not armstrong')