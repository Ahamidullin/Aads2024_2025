from math import gcd

n, q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
fractions = []
for a in A:
    for b in B:
        common_divisor = gcd(a, b)
        reduced_numerator,reduced_denominator = a // common_divisor,b // common_divisor
        fractions.append((reduced_numerator, reduced_denominator))

fractions.sort(key=lambda x: (x[0] / x[1]))


for c in C:
    idx = c - 1
    print(f"{fractions[idx][0]} {fractions[idx][1]}")
