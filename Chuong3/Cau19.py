from math import factorial

print("\nChương trình tính S(x, n) = x^(2n+1) / (2n+1)!\n")
x = int(input('Nhập x = '))
n = int(input('Nhập n = '))
s = 0
for i in range (0, n+1):
    s += x**(2*i+1) / factorial(2*i+1)
print('Kết quả S({0}, {1}) = {2}'.format(x, n, s))