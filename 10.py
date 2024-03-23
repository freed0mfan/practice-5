PIN = input('Придуманный PIN-код: ')

if PIN.count(PIN[0]) == 1 and PIN.count(PIN[1]) == 1 and PIN.count(PIN[2]) == 1:
    if len(PIN) == 4 and int(PIN) not in range(1900, 2051):
        print('OK')
else:
    print('ERROR')


