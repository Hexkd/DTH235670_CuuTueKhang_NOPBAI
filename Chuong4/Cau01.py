from math import sqrt
print('\nChương trình tính diện tích tam giác\n')

a = int(input('Nhập cạnh a>0: '))
b = int(input('Nhập cạnh b>0: '))
c = int(input('Nhập cạnh c>0: '))

if(a<0 or b<0 or c<0 or (a+b)<=c or (a+c)<=b or (b+c)<=a):
    print('\nTam giác không hợp lệ!\n')
else:
    cv = a+b+c
    p = cv/2
    dt = sqrt(p*(p-a)*(p-b)*(p-c))
    print('\nDiện tích = {0}'.format(dt))