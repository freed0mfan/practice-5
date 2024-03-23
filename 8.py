N = float(input('N: '))
sikl = N // 29
galleon = N // (29*17)

if galleon > 0:
    print(f'{int(galleon // 1)} галлеонов')
if sikl - (galleon // 1)*17 > 0:
    print(f'{int(sikl - (galleon // 1)*17)} сиклей')
if N - sikl * 29 > 0:
    print(f'{int(N - sikl * 29)} кнатов')
