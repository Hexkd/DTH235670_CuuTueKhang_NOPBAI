from random import randrange

print('Game Đoán Số')
while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False
    while solandoan < 7:
        solandoan+=1
        songuoi = int(input('Máy đoán [1..100], mời bạn đoán: '))
        print('Bạn đoán lần thứ {0}'.format(solandoan))
        if (somay == songuoi):
            print('\nChúc mừng bạn đoán đúng, số máy là = {0}'.format(somay))
            win = True
            break
        elif (somay > songuoi):
            print('Bạn đoán sai, số máy > số của bạn')
        elif (somay < songuoi):
            print('Bạn đoán sai, số máy < số của bạn')
    if (win == False):
        print('\nGAME OVER!\nSố máy = {0}'.format(somay))
    while hoi != 'c' or hoi != 'k':
        hoi = input('Tiếp tục? (c/k)')
    if (hoi == 'k'):
        break
print('\nCảm ơn bạn đã chơi game!\n')