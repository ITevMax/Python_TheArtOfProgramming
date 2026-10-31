# def pal(s : str) -> str:
#     if len(s) <= 1:
#         return s
#     if s[0] == s[-1]:
#         return s[0] + pal(s[1:-1]) + s[-1]
#     else:
#         a = pal(s[:-1])
#         b = pal(s[1:])
#         if len(a) >= len(b):
#             return a
#         else:
#             return b

# s = "abxyvxa" #"axyxa"
# print(pal(s))


# D = {}

# def pal(s : str) -> str:
#     if s not in D:
#         if len(s) <= 1:
#             D[s] = s
#         elif s[0] == s[-1]:
#             D[s] = s[0] + pal(s[1:-1]) + s[-1]
#         else:
#             a = pal(s[:-1])
#             b = pal(s[1:])
#             if len(a) >= len(b):
#                 D[s] = a
#             else:
#                 D[s] = b
#     return D[s]

# s = "abxyvxa" #"axyxa"
# print(pal(s))


# D = {}

# def pal(s : str, L = 0, R = None) -> str:
#     if R is None:
#         R = len(s) - 1
#     if (s, L, R) not in D:
#         if L > R:
#             D[s, L, R] = ""
#         elif L == R:
#             D[s, L, R] = s[L]
#         elif s[L] == s[R]:
#             D[s, L, R] = s[L] + pal(s, L + 1, R - 1) + s[R]
#         else:
#             a = pal(s, L, R - 1)
#             b = pal(s, L + 1, R)
#             if len(a) >= len(b):
#                 D[s, L, R] = a
#             else:
#                 D[s, L, R] = b
#     return D[s, L, R]

# s = "abxyvxa" #"axyxa"
# print(pal(s))

# s = "казак" #"казак"
# print(pal(s))


# def square(M, y = 0, x = 0, L = None, S = {}):
#     if L is None:
#         L = len(M)
#         S = {}
#     if (y, x, L) in S:
#         f = True
#         for i in range(y, y + L):
#             for j in range(x, x + L):
#                 if M[i][j] != 1:
#                     f = False
#                     break
#             if f == False:
#                 break
#         if f:
#             return L
#         else:
#             S[y, x, L] = max(square(M, y + 1, x + 1, L - 1, S),
#                             square(M, y + 1, x, L - 1, S),
#                             square(M, y, x + 1, L - 1, S),
#                             square(M, y, x, L - 1, S))
#     return S[y, x, L]

# M = [[0, 0, 1, 0, 0],
#      [1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 0],
#      [1, 0, 0, 0, 0],
#      [1, 0, 0, 1, 1]]

# print(square(M))