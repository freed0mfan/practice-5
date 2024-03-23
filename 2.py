import turtle as t
import math as m

x0 = int(input('x0 = '))
y0 = int(input('y0 = '))
r = int(input('r = '))

t.teleport(x0, y0-r)
t.circle(r)

x = int(input('x = '))
y = int(input('y = '))

t.teleport(x, y)
t.dot(5, 'RED')

t.color('RED')
d = m.sqrt((x-x0)**2 + (y-y0)**2)
if d < r:
    t.write('Точка внутри окружности')
elif d == r:
    t.write('Точка на окружности')
else:
    t.write('Точка вне окружности')

t.ht()
t.done()

