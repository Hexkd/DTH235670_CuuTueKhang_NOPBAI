# Viết chương trình tính logarit cơ số a của x
from math import log
print("\nChương trình tính logarit cơ số a của x\n")
x = float(input("Nhập giá trị x (x > 0):"))
a = float(input("Nhập giá trị a (a > 0 và a ≠ 1):"))
if x <= 0 or a <= 0 or a == 1:
    print("Giá trị x hoặc a không hợp lệ. Vui lòng nhập lại.")
else:
    log_a_x = log(x, a)
    print("\nLogarit cơ số {0} của {1} là: log_{0}({1}) = {2}".format(a, x, log_a_x))