"""
Homework, task 3 for lesson
"""
# 1) Создать класс, в конструктор которого передается одно число
# В этом классе должен быть метод show, который распечатывает
# переданное число.

class ShowValue:
    def __init__(self, value):
        self.data = value

    def show(self):
        print("The value is ",self.data)
a = ShowValue(2)
a.show()

# 2) Создать класс, который наследуется от предыдущего класса и в этот класс передается два числа.
# Данный класс реализует метод calc, который складывает эти два числа.
class PlusValue(ShowValue):
    def __init__(self, value1, value2):
        self.data1 = value1
        self.data2 = value2
    def show(self):
        print("First value is {0}, second value is {1}".format(self.data1, self.data2))

    def plus(self):
        print("Sum of {0} and {1}: ".format(self.data1, self.data2), self.data1 + self.data2)
a = PlusValue(2,5)
a.show()
a.plus()

# 3) Создать блок try/except/finally
# Внутри блока try создать выражение, которое делит на 0.
# Перехватить эту ошибку и распечатать сообщение пользователю.
try:
    a = 10
    b = 0
    c = a/b     #Деление на ноль
    print("All fine")
except ZeroDivisionError:
    print("Division by zero!!!")
finally:
    print("It is final block")

# 4) Создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции.
def PrintArgs(func):
    def inner(*args, **kwargs):
        if args:
            print("Arguments of this functions: ", args)
        if kwargs:
            print("Keyword arguments of this functions: ", kwargs)
        return func(*args, **kwargs)
    return inner

@PrintArgs
def function(x, y, z):
    print("Sum:", x+y+z)
    return x+y+z

function(1,2,3)
function(1,2,z = 3)

# 5) Создать класс, в котором применяется декоратор  @property для доступа к внутренней переменной.
class GetASum:
    def __init__(self, value1, value2):
        self.data1 = value1
        self.data2 = value2

    @property
    def sum(self):
        a = self.data1 + self.data2
        print('Sum: ', a)
        return a
c = GetASum(3,4)
c.sum

# 6) Создать генератор, который возвращает числа от 1 до 10
def gen(n):
    while n <= 10:
        yield n
        n += 1

for i in gen(1):
    print("i = ", i)

# 7) С помощью стандартной функции collections.namedtuple создать объект для хранения точки в трехмерном пространстве.
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(x = 1, y = 2, z = 3)
print("Значение по оси x = {0}, y = {1}, z = {2}".format(p.x, p.y, p.z))

# 8) Создать пакет, в котором будет  (можно использовать пакет datetime).
# Для данного пакета подготовить setup.py для установки.
# Создан пакет TestPackage
