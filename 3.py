num = int(input('Четырехзначное число: '))
dgt_1 = num // 1000
dgt_2 = (num // 100) % 10
dgt_3 = (num // 10) % 10
dgt_4 = num % 10

if dgt_1 == dgt_4 and dgt_2 == dgt_3:
    print('Настоящее')
else:
    print('Кривое')
