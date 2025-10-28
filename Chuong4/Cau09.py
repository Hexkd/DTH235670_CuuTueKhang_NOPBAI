# Chương trình tính căn bậc 2 lồng nhau n lần
from math import sqrt
print("\nChương trình tính căn bậc 2 lồng nhau\n")
n = int(input("Nhập số lần lồng nhau n (n ≥ 0): "))
if n < 0:
    print("\nGiá trị n không hợp lệ. Vui lòng nhập lại.\n")
else:
    for i in range(n):
        x = sqrt(2 + x) if i > 0 else sqrt(2)
    if n == 0:
        x = sqrt(2)
    print("\nKết quả căn bậc 2 lồng nhau \'{0}\' lần là: {1}".format(n, x))