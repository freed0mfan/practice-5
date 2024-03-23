num = int(input('Число: '))
parrot = ' '

if (num // 10) % 10 != 1:
    if num % 10 == 1:
        parrot = 'попугай'
    elif 1 < num % 10 < 5:
        parrot = 'попугая'
    elif 4 < num % 10 or num % 10 == 0:
        parrot = 'попугаев'
else:
    parrot = 'попугаев'

print(f'{num} {parrot}')
