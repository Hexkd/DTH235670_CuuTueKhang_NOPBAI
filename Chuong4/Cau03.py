def BMI(height, weight):
    return (weight / (height**2))

def PhanLoai(bmi):
    if bmi < 18.5:
        return 'Gầy'
    elif bmi < 25:
        return 'Bình thường'
    elif bmi < 30:
        return 'Hơi béo'
    elif bmi < 35:
        return 'Béo phì cấp độ 1'
    elif bmi < 40:
        return 'Béo phì cấp độ 2'
    else:
        return 'Béo phì cấp độ 3'

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return 'Thấp'
    elif bmi < 25:
        return 'Trung bình'
    elif bmi < 35:
        return 'Cao'
    elif bmi < 40:
        return 'Rất cao'
    else:
        return 'Nguy hiểm'

print('\nChương trình tính chỉ số BMI (kg/m²)\n')
height = float(input('Nhập chiều cao (m): '))
weight = float(input('Nhập cân nặng (kg): '))

bmi = BMI(height, weight)

print("\n>>> Kết quả <<<")
print("Chỉ số BMI của bạn: {0}".format(bmi)) 
print("Phân loại thể trạng: {0}".format(PhanLoai(bmi))) 
print("Nguy cơ mắc bệnh của bạn: {0}".format(NguyCoBenh(bmi)))