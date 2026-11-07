class point:                                                #Создание класса точки
    def __init__(self, x = 0, y = 0):                       #Конструктор для создания экземпляра
        self.x = x                                          #Присвоение значения полю x и y
        self.y = y
    
    def input(self):                                        #Метод для ввода значений x и y из консоли
        s = input().split()                                 #Чтение ввода и разбиение на x и y
        self.x = float(s[0])                                #Привязки значений к полям
        self.y = float(s[1])
        return self                                         #Возврат нового объекта point со своими значениями полей
    

def dist(A : point, B : point):                             #Метод для подсчёта расстояния между точками (По теореме Пифагора)
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5


class triangle:                                             #Создание класса треугольника
    def __init__(self, A = None, B = None, C = None):       #Конструктор для создания экземпляра
        if A == None:                                       #Если значение не передавалось, то вызывается метод для
                                                            #создания экземпляра по значениям из консоли
            self.A = point().input()
        else:
            self.A = A
        if B == None:
            self.B = point().input()
        else:
            self.B = B
        if C == None:
            self.C = point().input()
        else:
            self.C = C
    
    def input(self):                                        #Метода для ввода координат точек треугольника
        self.A.input()
        self.B.input()
        self.C.input()
        return self
    
    def perim(self) -> float:                               #Подсчёт периметра треугольника (и округление до 3 цифр после запятой)
        return round(dist(self.A, self.B) + dist(self.C, self.B) + dist(self.A, self.C), 3)
    
    def area(self) -> float:                                #Подсчёт площади треугольника (и округление до 3 цифр после запятой)
        p = self.perim() / 2                                #Полупериметр для поиска площади по формуле Герона (S = sqrt(p(p - a)(p - b)(p - c)))
        return round((p * (p - dist(self.A, self.B)) * (p - dist(self.C, self.B)) * (p - dist(self.A, self.C))) ** 0.5, 3)


A = point(2, 2)             #Создание экземпляров точек для примера
B = point(2, 8)
C = point(10, 2)
triang = triangle(A, B, C)  #Создание экземпляра треугольника с текущими точками
print(triang.perim())       #Вывод периметра
print(triang.area())        #Вывод площади