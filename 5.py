mass = float(input('Масса тела [кг]: '))
height = float(input('Рост [м]: '))
index = mass / (height ** 2)

if index < 16:
    print('Выраженный дефицит массы тела')
elif 16 <= index < 18.5:
    print('Недостаточная масса тела')
elif 18.5 <= index < 25:
    print('Норма')
elif 25 <= index < 30:
    print('Избыточная масса тела')
elif 30 <= index < 35:
    print('Ожирение I степени')
elif 35 <= index < 40:
    print('Ожирение II степени')
else:
    print('Ожирение III степени')
