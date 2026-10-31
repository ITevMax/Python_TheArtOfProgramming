# n! = 1 * 2 * 3 * ... * (n - 1) * n

# def f(n):
#     r = 1
#     for i in range(1, n + 1):
#         r = r * i
#         return r

# print(f(5))


# def fact(n):
#     if n == 1: return 1
#     return fact(n - 1) * n

# print(fact(5))


# from sys import setrecursionlimit

# setrecursionlimit(1500)

# def fact(n):
#     if n <= 2: return 2
#     return fib(n - 2) + fib(n - 1)

# print(fact(1100))


# def fib(n):
#     L = [0, 1]
#     for i in range(2, n + 1):
#         L.append(L[-2] + L[-1])
#     return L[-1]

# print(fib(10))


# def fib(n):
#     a, b = 1
#     r = 1
#     for i in range(3, n + 1):
#         r = a + b
#         a = b
#         b = r
#     return r

# print(fib(10))


# F = {}

# def fib(n):
#     if n not in F:
#         if n <= 2:
#             F[n] = 1
#         else:
#             F[n] = fib(n - 2) + fib(n - 1)
#     return F[n]

# print(fib(10))


# from functools import cache

# @cache
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)

# print(fib(10))


# def power(a, n):
#     if n == 1:
#         return a
#     elif n % 2 == 0:
#         return power(a, n / 2) * power(a, n / 2)
#     else:
#         return a * power(a, n - 1)

# print(power(2, 10))


# D = {}

# def power(a, n):
#     if (a, n) not in D:
#         if n == 1:
#             D[a, n] = a
#         elif n % 2 == 0:
#             D[a, n] = power(a * a, n // 2)
#         else:
#             D[a, n] = a * power(a, n - 1)
#     return D[a, n]

# print(power(3, 8))


