# Cho biết bao nhiêu dấu * được in ra trên màn hình
# Biến a được khởi tạo với giá trị a=20 với điều kiện a<100 và sau khi thực hiện a=a+5
# Vậy có ((100 - 20 + 1 - 1) / 5) = 16 dấu * được in ra màn hình
# "+ 1" vì bắt đầu từ 20
# "- 1" vì kết thúc tại <100 (không tính 100)
for a in range (20, 100, 5):
    print('*', end='')
print()