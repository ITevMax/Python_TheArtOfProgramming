# s = "aaaabbc"
# n = 0
# for b in set(s):
#     if s.count(b) % 2 == 1:
#         n += 1
# if n > 1:
#     print("Нелья составить палиндром")
# else:
#     print("Можно составить палиндром")


# s = "aaaabbc"
# n = sum(1 for b in set(s) if s.count(b) % 2 == 1)
# if n > 1:
#     print("Нелья составить палиндром")
# else:
#     print("Можно составить палиндром")


# s = "aaaabbc"
# n = sum(s.count(b) % 2 for b in set(s))
# if n > 1:
#     print("Нелья составить палиндром")
# else:
#     print("Можно составить палиндром")


# D = {"a": 3, "b": 2, "ce": 4}
# print(D)

# print(D["a"])
# print(D["b"])
# print(D["ce"])

# print(list(D.keys()))
# print(list(D.values()))

# for key in D:
#     print(key, D[key])


# s = "aaaabbc"
# n = sum(s.count(b) % 2 for b in set(s))
# if n > 1:
#     print("Нелья составить палиндром")
# else:
#     print("Можно составить палиндром:", end=" ")
#     D = {}
#     for b in set(s):
#         D[b] = s.count(b)
#     p = ""
#     for b in D:
#         p += b * (D[b] // 2)
#     c = ""
#     for b in D:
#         if D[b] % 2 == 1:
#             c = b
#     p += c + p[::-1]
#     print(p)


# s = "aaaabbc"
# n = sum(s.count(b) % 2 for b in set(s))
# if n > 1:
#     print("Нелья составить палиндром")
# else:
#     print("Можно составить палиндром:", end=" ")
#     D = {b: s.count(b) for b in set(s)}
#     p = "".join(b * (D[b] // 2) for b in D)
#     c = "".join(b for b in D if D[b] % 2 == 1)
#     p += c + p[::-1]
#     print(p)


# from collections import Counter

# s = "aaaabbbbbbbbc"
# n = sum(s.count(b) % 2 for b in set(s))
# if n > 1:
#     print("Нелья составить палиндром")
# else:
#     print("Можно составить палиндром:", end=" ")
#     D = dict(Counter(s))
#     print(D)
#     p = ""
#     for b in D:
#         p += b * (D[b] // 2)
#     c = ""
#     for b in D:
#         if D[b] % 2 == 1:
#             c = b
#     p += c + p[::-1]
#     print(p)


# M = [[1, 8, 11, 14],
#      [12, 13, 2, 7],
#      [6, 3, 16, 9],
#      [15, 10, 5, 4]]

# n = len(M)
# d1 = 0
# for i in range(n):
#     d1 += M[i][i]

# d2 = 0
# for i in range(n):
#     d2 += M[-i][-1 - i]
# print(d1, d2)

# f = True
# if d1 == d2:
#     for i in range(n):
#         s = 0
#         for j in range(n):
#             s += M[i][j]
#         if d1 != s:
#             f = False
#             break
# else:
#     f = False

# if f:
#     print("Магический")
# else:
#     print("Обычный")


# M = [[1, 8, 11, 14],
#      [12, 13, 2, 7],
#      [6, 3, 16, 9],
#      [15, 10, 5, 4]]

# n = len(M)
# d1 = sum(M[i][i] for i in range(n))
# d2 = sum(M[i][-1 - i] for i in range(n))

# f = True
# if d1 == d2:
#     for i in range(n):
#         if d1 != sum(M[i]):
#             f = False
#             break
#     if f:
#         for i in range(n):
#             s = sum(M[j][i] for j in range(n))
#             if d1 != s:
#                 f = False
#                 break
# else:
#     f = False

# if f:
#     print("Магический")
# else:
#     print("Обычный")


# A = {"a", "b", "c", "d"}
# B = {"c", "d", "e", "f"}
# print(A | B)
# print(A & B)
# print(A - B)
# print(B - A)
# print(B ^ A)


# M = [[1, 8, 11, 14],
#      [12, 13, 2, 7],
#      [6, 3, 16, 9],
#      [15, 10, 5, 4]]

# n = len(M)
# D = {sum(M[i][i] for i in range(n)), sum(M[i][-1 - i] for i in range(n))}
# R = {sum(M[i]) for i in range(n)}
# C = {sum(M[j][i] for j in range(n)) for i in range(n)}

# S = D | R | C

# if len(S) == 1:
#     print("Магический")
# else:
#     print("Обычный")


# M = [[1, 8, 11, 14],
#      [12, 13, 2, 7],
#      [6, 3, 16, 9],
#      [15, 10, 5, 4]]

# n = len(M)

# print("Магический" if len({sum(M[i][i] for i in range(n)),
#                            sum(M[i][-1 - i] for i in range(n))} | 
#                           {sum(M[i]) for i in range(n)} |
#                           {sum(M[j][i] for j in range(n)) for i in range(n)}) == 1
#     else "Обычный")


# from numpy import array

# M = array([[1 , 8 , 11, 14],
#            [12, 13, 2 , 7 ],
#            [6 , 3 , 16, 9 ],
#            [15, 10, 5 , 4 ]])

# print(M)
# print(M[1, 2])
# print(M[1, :])
# print(M[:, 2])
# print(M[-1:1, -1:1])


# from numpy import array

# M = array([[1 , 8 , 11, 14],
#            [12, 13, 2 , 7 ],
#            [6 , 3 , 16, 9 ],
#            [15, 10, 5 , 4 ]])

# n = len(M)
# print("Магический" if len({sum(M[i, i] for i in range(n)),
#                            sum(M[i,-1 - i] for i in range(n))} | 
#                           {sum(M[i, :]) for i in range(n)} |
#                           {sum(M[:, i]) for i in range(n)}) == 1
#     else "Обычный")