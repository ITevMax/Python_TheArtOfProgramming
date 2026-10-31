# n = 100
# L = [i for i in range(n)]
# for i in range(2, n):
#     if L[i] != None:
#         for j in range(i + i, n, i):
#             L[j] = None

# print(L)


# n = 100
# L = [i for i in range(n)]
# for i in range(2, n):
#     if L[i] != None:
#         for j in range(i + i, n, i):
#             L[j] = None

# M = [el for el in L if el != None]
# print(M)


# n = 100
# L = [i for i in range(n)]
# for i in range(2, int(n**0.5) + 1):
#     if L[i] != None:
#         for j in range(i * i, n, i):
#             L[j] = None

# M = [el for el in L if el != None]
# print(M)


# n = 100
# L = [set() for i in range(n)]
# for i in range(2, n):
#     if len(L[i]) == 0:
#         for j in range(i + i, n, i):
#             L[j].add(i)

# for i in range(n):
#     print(i, L[i])


# from copy import copy
# from collections import defaultdict

# n=100
# L=[set() for i in range(n)]
# for i in range(2,n):
#     if len(L[i])==0:
#         for j in range(i,n,i):
#             L[j].add(i)
# M=[defaultdict(int) for i in range(n)]
# for i in range(2,n):
#     if L[i]=={i}:
#         M[i]={i:1}
#     else:
#         d=list(L[i])[0]
#         M[i]=copy(M[i//d])
#         M[i][d]+=1
# for i in range(n):
#     print(i, (M[i]))


# from copy import copy
# from collections import defaultdict

# def setdivider(n):
#     L=[set() for i in range(n)]
#     for i in range(2,n):
#         if len(L[i])==0:
#             for j in range(i,n,i):
#                 L[j].add(i)
#     return L

# def dictdivider(n):
#     L=setdivider(n)
#     M=[defaultdict(int) for i in range(n)]
#     for i in range(2,n):
#         if L[i]=={i}:
#             M[i][i]=1
#         else:
#             d=list(L[i])[0]
#             M[i]=copy(M[i//d])
#             M[i][d]+=1
#     return [dict(el) for el in M]

# def simple(n):
#     L=setdivider(n)
#     return [i for i in range(n) if L[i]=={i}]

# n=100
# print(simple(n))


# from copy import copy
# from collections import defaultdict

# def setdivider(n):
#     L=[set() for i in range(n)]
#     for i in range(2,n):
#         if len(L[i])==0:
#             for j in range(i,n,i):
#                 L[j].add(i)
#     return L

# def dictdivider(n):
#     L=setdivider(n)
#     M=[defaultdict(int) for i in range(n)]
#     for i in range(2,n):
#         if L[i]=={i}:
#             M[i][i]=1
#         else:
#             d=list(L[i])[0]
#             M[i]=copy(M[i//d])
#             M[i][d]+=1
#     return [dict(el) for el in M]

# def simple(n):
#     L=setdivider(n)
#     return [i for i in range(n) if L[i]=={i}]

# def onedivider(n):
#     M = dictdivider(n)
#     for i in range(n):
#         return [i for i in range(n) if all(el == 1 for el in M[i].values())]

# n=100
# print(onedivider(n))


