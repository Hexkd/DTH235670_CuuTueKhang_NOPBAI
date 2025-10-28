# Tinh khoảng cách giữa hai điểm A(xa, ya) và B(xb, yb) trong mặt phẳng Oxy
import math
print("\nChương trình tính khoảng cách giữa hai điểm A và B trong mặt phẳng Oxy\n")
xa = int(input("Nhập hoành độ điểm A: "))
ya = int(input("Nhập tung độ điểm A: "))
xb = int(input("Nhập hoành độ điểm B: "))
yb = int(input("Nhập tung độ điểm B: "))
d = math.sqrt((xb - xa)**2 + (yb - ya)**2)
print("\nKhoảng cách giữa hai điểm A và B là: d = {0}".format(d))