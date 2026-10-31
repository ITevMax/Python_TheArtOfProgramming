# def cache(f):
#     D = {}
#     def res(n):
#         if n not in D:
#             D[n] = f(n)
#         return D[n]
#     return res

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return fact(n - 1) * n

# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# fib = cache(fib)
# fact = cache(fact)

# print(fact(5))
# print(fib(40))


# def cache(f):
#     D = {}
#     def res(n):
#         if n not in D:
#             D[n] = f(n)
#         return D[n]
#     return res

# @cache
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return fact(n - 1) * n

# @cache
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fact(5))
# print(fib(40))


# def deco(f):
#     def res(s):
#         print("Питон рад тебя видеть!")
#         f(s)
#         print("Пока!")
#     return res

# @deco
# def hello(s):
#     print("Привет", s)

# s = input("Как тебя зовут?\n")
# hello(s)


# def createdeco(p):
#     def deco(f):
#         def res(s):
#             print("Питон рад тебя видеть", p)
#             f(s)
#             print("Пока!")
#         return res
#     return deco

# mister = createdeco("Господин")

# @mister
# def hello(s):
#     print("Привет", s)

# s = input("Как тебя зовут?\n")
# hello(s)


# def cache(f):
#     D = {}
#     def res(n):
#         if n not in D:
#             D[n] = f(n)
#         return D[n]
#     res.cache = D
#     return res

# @cache
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return fact(n - 1) * n

# @cache
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fact(5))
# print(fib(40))
# print(fib.cache)


# def cache(f):
#     D = {}
#     def res(*args):
#         if args not in D:
#             D[args] = f(*args)
#         return D[args]
#     res.cache = D
#     return res

# def log(f):
#     D = []
#     def res(*args):
#         D.append(args)
#         return f(*args)
#     res.log = D
#     return res

# @log
# @cache
# def fastpow(a, n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         return fastpow(a, n // 2) * fastpow(a, n // 2)
#     else:
#         return fastpow(a, n - 1) * a

# print(fastpow(2, 8))
# print(fastpow.log)


# def cache(f):
#     D = {}
#     def res(*args):
#         if args not in D:
#             D[args] = f(*args)
#         return D[args]
#     res.__dict__ = f.__dict__
#     res.cache = D
#     return res

# def log(f):
#     D = []
#     def res(*args):
#         D.append(args)
#         return f(*args)
#     res.__dict__ = f.__dict__
#     res.log = D
#     return res

# @log
# @cache
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fib(10))
# print(fib.log)
# print(fib.cache)
# print(fib.__dict__)


# def copydict(g):
#     def deco(f):
#         def res(n):
#             return f(n)
#         res.__dict__ = g.__dict__
#         return res
#     return deco

# def cache(f):
#     D = {}
#     @copydict(f)
#     def res(*args):
#         if args not in D:
#             D[args] = f(*args)
#         return D[args]
#     res.__dict__ = f.__dict__
#     res.cache = D
#     return res

# def log(f):
#     D = []
#     @copydict(f)
#     def res(*args):
#         D.append(args)
#         return f(*args)
#     res.__dict__ = f.__dict__
#     res.log = D
#     return res

# @log
# @cache
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fib(10))
# print(fib.log)
# print(fib.cache)
# print(fib.__dict__)
# print(fib.__name__)


# from functools import wraps

# def cache(f):
#     D = {}
#     @wraps(f)
#     def res(*args):
#         if args not in D:
#             D[args] = f(*args)
#         return D[args]
#     res.__dict__ = f.__dict__
#     res.cache = D
#     return res

# def log(f):
#     D = []
#     @wraps(f)
#     def res(*args):
#         D.append(args)
#         return f(*args)
#     res.__dict__ = f.__dict__
#     res.log = D
#     return res

# @log
# @cache
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# print(fib(10))
# print(fib.log)
# print(fib.cache)
# print(fib.__dict__)
# print(fib.__name__)


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

def dist(A : point, B : point):
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5

A = point(0, 0)
B = point().input()
print(dist(A, B))