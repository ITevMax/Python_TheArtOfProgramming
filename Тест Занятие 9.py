curryear = 2026         #Текущий год


class person:           #Создание класса Человек
    def __init__(self, firstname = "", lastname = "", year = 0):        #Инициализация экземпляра с параметрами по умолчанию
        self.firstname = firstname          #Присвоение значений полям имени фамилии и года рождения
        self.lastname = lastname
        self.year = year

    def __str__(self) -> str:           #Строковое представление экземпляра
        return f"{self.firstname} {self.lastname} {str(self.year)}"

    def __getfullname(self) -> str:         #Получение имени и фамилии человека
        return f"{self.firstname} {self.lastname}"

    fullname = property(__getfullname)      #Свойство класса с его именем и фамилией

    def age(self) -> int:           #Вычисление возраста человека
        return curryear - self.year

    @classmethod        #Метод класса
    def who(cls):       #Показываем принадлежность к классу и возраст человека
        return f"Я человек, мне {age(self)}"


class student(person):          #Создание класса Студент с наследованием от класса Человек
    def __init__(self, firstname = "", lastname = "", year = 0, enteryear = 0):     #Инициализация экземпляра
        super().__init__(firstname, lastname, year)         #Передаём часть параметров в базовый класс
        self.enteryear = enteryear          #Присвоение значение новому полю года поступления

    def age(self):          #Вычисление времени обучения
        return curryear - self.enteryear

    def who(self):          #Показываем принадлежность к классу, возраст и время обучения
        return f"Я студент {self.fullname}, мне {person.age(self)}, учусь уже {age()}"


class teacher(person):          #Создание класса Преподаватель с наследованием от класса Человек
    def __init__(self, firstname = "", lastname = "", year = 0, workyear = 0):      #Инициализация экземпляра
        super().__init__(firstname, lastname, year)         #Передаём часть параметров в базовый класс
        self.workyear = workyear             #Присвоение значение новому полю году начала работы

    def age(self):          #Вычисление времени работы
        return curryear - self.workyear

    def who(self):          #Показываем принадлежность к классу, возраст и время работы
        return f"Я учитель {self.fullname}, мне {person.age(self)}, работаю {age()}"


class postgrad(teacher, student):          #Создание класса Аспирант с наследованием от классов Преподаватель и Студент
    def __init__(self, firstname = "", lastname = "", year = 0, enteryear = 0, workyear = 0):   #Инициализация экземпляра
        teacher.__init__(self, firstname, lastname, year, workyear)         #Передаём часть параметров в базовый класс Преподаватель
        student.__init__(self, firstname, lastname, year, enteryear)        #Передаём часть параметров в базовый класс Студент

    def age(self):          #Возврат возраста человека
        return person.age(self)

    def who(self):          #Показываем принадлежность к классу, возраст, время учёбы и работы
        return f"""Я аспирант {self.fullname}, мне {person.age(self)}, учусь уже {student.age(self)} и работаю {teacher.age(self)}"""


#Пример работы:
s = postgrad("Артур", "Павлов", 2000, 2020, 2024) #Создание экземпляра аспиранта
print(s)
print(s.age())
print(s.who())

"""
Вывод:
Артур Павлов 2000
26
Я аспирант Артур Павлов, мне 26, учусь уже 6 и работаю 2
"""