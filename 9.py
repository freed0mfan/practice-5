towers = input('Высоты башен: ')
h1 = int(towers.split(' ')[0])
h2 = int(towers.split(' ')[1])
h3 = int(towers.split(' ')[2])

if h1 >= h2 >= h3:
    print(h1, h2, h3)
elif h1 >= h3 >= h2:
    print(h1, h3, h2)
elif h2 >= h1 >= h3:
    print(h2, h1, h3)
elif h2 >= h3 >= h1:
    print(h2, h3, h1)
elif h3 >= h1 >= h2:
    print(h3, h1, h2)
else:
    print(h3, h2, h1)
