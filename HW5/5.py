from itertools import product
n = int(input())

cnt = 0
for i in product('XY',repeat = n):
    i = ''.join(i)
    if ('YY' not in i):
        print(''.join(i))
        cnt +=1
print(cnt)