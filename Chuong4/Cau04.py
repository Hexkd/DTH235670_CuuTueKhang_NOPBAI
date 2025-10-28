def ROI(dt, cp):
    return (dt-cp)/cp
def GoiYDauTu(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

print('\nChương trình tính ROI\n')
dt = int(input('Nhập Doanh Thu: '))
cp = int(input('Nhập Chi Phí  : '))
roi = ROI(dt, cp)
print('Tỉ lệ ROI = {0}'.format(roi))
print('==> ', GoiYDauTu(roi))