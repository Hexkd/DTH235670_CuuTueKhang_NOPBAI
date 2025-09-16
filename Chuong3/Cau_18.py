# Vẽ các hình

n = int(input('\n\n\nNhập chiều cao n = '))


print('\n')


# Hình vuông rỗng
for i in range (0, n):
    if (i == 0 or i == n-1): # in không khoảng trống
        for i1 in range (0, n):
            print('* ', end='')
    else: # in có khoảng trống
        print('* ', end='')
        for i2 in range (1, n-1):
            print('  ', end='')
        print('* ', end='')
    print() # Xuống dòng


print('\n')


# Hình tam giác vuông phải
for i in range (n, 0, -1):
    for k in range (0, i-1):
        print('  ', end='')
    for j in range (0, n-i+1):
        print('* ', end='')
    print() # Xuống dòng


print('\n')


# Hình tam giác có nghịch đảo từ đáy góc xuống đỉnh (giống như hình tia chớp với 2 tam giác rỗng)
for i in range (0, n):
    if (i <= 2): # in không khoảng trống
        for i1 in range (0, i):
            print('* ', end='')
    else: # in có khoảng trống
        print('* ', end='')
        for i2 in range (1, i-1):
            print('  ', end='')
        print('* ', end='')
    print() # Xuống dòng
for k in range (0, 2*n-1):
    print('* ', end='')
print() # Xuống dòng
for j in range (n-1, 0, -1):
    for j1 in range(0, n):
        print('  ', end='')
    for j2 in range (0, n-j-1):
        print('  ', end='')
    if (j <= 2): # in không khoảng trống
        for j3 in range (0, j):
            print('* ', end='')
    else: # in có khoảng trống
        print('* ', end='')
        for j4 in range (1, j-1):
            print('  ', end='')
        print('* ', end='')
    print() # Xuống dòng


print('\n')