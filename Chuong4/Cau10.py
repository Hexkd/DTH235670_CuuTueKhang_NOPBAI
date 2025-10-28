# Vẽ hình dùng Sleep, dùng sleep để xuất hiện từng hình sau 5 giây
from time import sleep
print("\nChương trình vẽ hình dùng Sleep\n")
n = 5 # Độ lớn hình
t = int(input("Nhập thời gian chờ giữa từng hình: "))

print()
# Hình 1
for i in range(n):
    for i1 in range(n-1):
        print('  ', end='')
    for j in range(i):
        print("* ", end='')
    print()
for m in range(2*n-1):
    print('* ', end='')
print()
for i in range(n-1):
    for i2 in range(n - i - 1):
        print('* ', end='')
    for j2 in range(i):
        print("  ", end='')
    print()

sleep(t)

print()
# Hình 2
for i in range(n):
    for i1 in range(n-1):
        print('  ', end='')
    if i < 2:
        for j in range(i):
            print("* ", end='')
    else:
        print("* " , end='')
        for j in range(i - 2):
            print("  ", end='')
        print("* ", end='')
    print()
for m in range(2*n-1):
    print('* ', end='')
print()
for i in range(n):
    if i >= n - 2:
        for i2 in range(n - i - 1):
            print('* ', end='')
        print()
    else:
        print("* ", end='')
        for j2 in range(n - i - 2 - 1):
            print("  ", end='')
        print("* ", end='')
        print()
    
sleep(t)

print()
# Hình 3
for i in range(n):
    for i1 in range(n - 1):
        print('  ', end='')
    for j1 in range(n - i):
        print("* ", end='')
    print()
for i in range(n):
    # Bỏ qua dòng đầu tiên
    if i == 0:
        continue
    for i2 in range(n - i - 1):
        print('  ', end='')
    for j2 in range(i + 1):
        print("* ", end='')
    print()

sleep(t)

print()
# Hình 4
temp = True
for i in range(n):
    for i1 in range(n - 1):
        print('  ', end='')

    # In hàng đầu tiên chỉ một lần
    if temp:
        for top in range(n):
            print('* ', end='')
        print()
        temp = False # Đánh dấu đã in hàng đầu tiên
        continue

    # # test
    # if i == 0 or i >= n - 2:
    #     for i1 in range(n-i-1):
    #         print("* ", end='')
    #     print()
    # else:
    #     print("* ", end='')
    #     for j in range(n-i):
    #         for j in range(n - 2):
    #             print("  ", end='')
    #         print("* ", end='')
    #         print()

    # In các hàng còn lại
    print("* ", end='')
    for j in range(n-i-2):
        print("  ", end='')
    if i != n - 1:
        print("* ", end='')
    print()
for i in range(n):
    # Bỏ qua dòng đầu tiên
    if i == 0 or i == n-1:
        continue
    for i1 in range(n-i-1):
        print('  ', end='')
    if i < 2:
        for j1 in range(n-i-2):
            print('* ', end='')
    else:
        print('* ', end='')
        for j2 in range(i-1):
            print('  ', end='')
        print('* ', end='')
    print()
for bottom in range(n):
    print('* ', end='')