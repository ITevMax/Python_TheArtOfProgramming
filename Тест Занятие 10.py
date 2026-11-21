class Vector:                           #Создание класса Вектор
    def __init__(self, x=0.0, y=0.0):   #Инициализация экземпляра с параметрами по умолчанию
        self.x = x                      #Присвоение соответсвующих значений полям x и y
        self.y = y
    
    def __add__(self, v2):              #Метод сложения векторов
        return Vector(self.x + v2.x, self.y + v2.y)     #При этом создаётся новый вектор
    
    def __mul__(self, v2):              #Метод скалярного умножения векторов
        return self.x * v2.x + self.y + v2.y
    
    def mod(self):                      #Метод нахождения модуля с округлением до 5 знаков после запятой
        return round((self.x * self.x + self.y * self.y) ** 0.5, 5)
    
    def __str__(self):                  #Строковое представление экземпляра в виде его координат
        return f"({self.x}, {self.y})"


#Пример работы
a = Vector(6, 8)
b = Vector(4, 10)
print(a.__add__(b))
print(a.__mul__(b))
print(a.mod())
print(b.mod())
'''
Результат:
(10, 18)
42
10.0
10.77
'''