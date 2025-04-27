# from functools import lru_cache
# from fractions import Fraction
#
# @lru_cache(None)
# def P(a, b):
#     if a == 10:
#         return Fraction(1)
#     if b == 16:
#         return Fraction(0)
#     return (Fraction(a, a + b) * P(a + 1, b)) + (Fraction(b, a + b) * P(a, b + 1))
#
# print(P(1, 1))

# from math import lcm
#
# for N in range(251, 1000):
#     good = True
#     for n in range(1, 1000000000):
#         lcm1 = lcm(*[n + i for i in range(1, 11)])
#         lcm2 = lcm(*[n + i for i in range(10)])
#         if (N * lcm1) < lcm2:
#             good = False
#             break
#     if good:
#         print(N)
#         break

from math import lcm, ceil
searching = True
N = 1
start = 1
while searching:
    searching = False
    for n in range(start, 1000000000):
        lcm1 = lcm(*[n + i for i in range(1, 11)])
        lcm2 = lcm(*[n + i for i in range(10)])
        if (N * lcm1) < lcm2:
            start = n
            N = ceil(lcm2 / lcm1)
            print(N)
            searching = True
            break
    if not searching:
        print("RESULT", N)
        break






