print('Введите коэффициенты для уравнения ax^2 + bx + c:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
D = b**2 - 4 * a * c

if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print(x1,x2)

if D == 0:
    x = (-b) / (2*a)
    print(x)

if D < 0:
    print('корней нет')




