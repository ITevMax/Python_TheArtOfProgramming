curryear = 2026

class person:
    n = 0
    def __init__(self, firstname = "", lastname = "", year = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.__class__.n = self.__class__.n + 1

    def __str__(self):
        return self.fullname + " " + str(self.year)

    def __getfullname(self):
        return self.firstname + " " + self.lastname

    def __setfullname(self, s):
        self.firstname, self.lastname = s.split()

    fullname = property(__getfullname, __setfullname)
    @property
    def age(self):
        return curryear - self.year

    @classmethod
    def who(cls):
        print(f"Я человек! Нас {cls.n} человек")



class student(person):
    n = 0
    def __init__(self, firstname = "", lastname = "", year = 0, yearenter = 0):
        super().__init__(firstname, lastname, year)
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.yearenter = yearenter

    def age(self):
        return curryear - self.yearenter


p1 = student("Иван", "Петров", 2000, 2024)
p2 = student("Мария", "Петрова", 2001, 2024)
print(p1.age())
print(p2.age())