# n = int(input())
# s = 0
# f = 1
# for i in range(1, n + 1):
#     f *= i
#     s += f
# print(s)


# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f

# def sumfact(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += fact(i)
#     return s

# n = int(input())
# print(sumfact(n))


# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f

# F = {}
# def sumfact(n):
#     if n not in F:
#         s = 0
#         for i in range(1, n + 1):
#             s += fact(i)
#         F[n] = s
#     return F[n]

# n = int(input())
# print(sumfact(n))


# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f

# def sigma(n, f):
#     s = 0
#     for i in range(1, n + 1):
#         s += f(i)
#     return s

# n = int(input())
# print(sigma(n, fact))


# def simple(n):
#     return n

# def pi(n, f):
#     s = 1
#     for i in range(1, n + 1):
#         s *= f(i)
#     return s

# def fact(n):
#     return pi(n, simple)

# def sigma(n, f):
#     s = 0
#     for i in range(1, n + 1):
#         s += f(i)
#     return s

# n = int(input())
# print(sigma(n, fact))


# def row(n, f, s, b):
#     for i in range(1, n + 1):
#         s = b(s, f(i))
#     return s

# def fact(n):
#     return row(n, lambda n : n, 1, lambda a, b : a * b)

# n = int(input())
# print(row(n, fact, 0, lambda a, b : a + b))


# L = [1, -2 ,3, -4, 5]
# M = []
# for el ni L:
#     if el > 0:
#         M.append(el)

# print(M)


# L = [1, -2 ,3, -4, 5]
# M = [el for el in L if el > 0]
# print(M)


# def positive(n):
#     return n > 0

# L = [1, -2 ,3, -4, 5]
# M = list(filter(positive, L))
# print(M)


# positive = lambda n: n > 0

# L = [1, -2 ,3, -4, 5]
# M = list(filter(positive, L))
# print(M)


# L = [1, -2 ,3, -4, 5]
# M = list(filter(lambda n: n > 0, L))
# print(M)


# L = [0, 1, 2, 3, 4, 5]
# M = []

# for el in L:
#     M.append(el ** 2)

# print(M)


# L = [0, 1, 2, 3, 4, 5]
# M = [el ** 2 for el in L]
# print(M)


# def square(n):
#     return n ** 2

# L = [0, 1, 2, 3, 4, 5]
# print(list(map(square, L)))


# L = [0, 1, 2, 3, 4, 5]
# print(list(map(lambda n: n ** 2, L)))


# from functools import reduce

# L = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x * y, L))


# L = [[5, 6], [4, 7], [3, 8], [2, 9], [1, 10]]
# print(sorted(L))
# print(sorted(L, key = lambda el: el[1]))


from functools import reduce
from operator import mul

n = int(input())
print(sum(map(lambda n : reduce(mul, range(1, n + 1), 1), range(1, n + 1))))