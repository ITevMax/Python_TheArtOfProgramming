class point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def input(self):
        s = input().split()
        self.x = float(s[0])
        self.y = float(s[1])
        return self

    def __str__(self):
        return f"({self.x}, {self.y})"

class section:
    def __init__(self, A = None, B = None):
        if A == None:
            self.A = point()
        if B == None:
            self.B = point()
        else:
            self.B = B

    def input(self):
        self().A.input()
        self().B.input()
        return self

    def __str__(self):
        return f"[{str(self.A)},{str(self.B)},{str(self.c)}]"


class section:
    def __init__(self, A = None, B = None):
        if A == None:
            self.A = point()
        if B == None:
            self.B = point()
        else:
            self.B = B
    
    def input(self):
        self().A.input()
        self().B.input()
        return self
    
    def __str__(self):
        return f"[{str(self.A)},{str(self.B)},{str(self.c)}]"
    
    @property
    def perim(self):
        return dist(self.A, self.B) + dist(self.A, self.C) + dist(self.C, self.B)

    @property
    def area(self):
        p = self.perim() / 2
        return (p * (p - dist(self.A, self.B) * dist(self.A, self.C) * dist(self.C, self.B)))


def dist(A : point, B : point):
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5

A = point(0, 0)
B = point().input()
print(dist(A, B))