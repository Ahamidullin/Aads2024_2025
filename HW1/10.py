import heapq
def f(a):
    heapq.heapify(a)
    suma = 0.00
    while len(a) != 1:
        x = heapq.heappop(a)
        y = heapq.heappop(a)

        currentSuma = x + y
        heapq.heappush(a,currentSuma)
        cost = (currentSuma * 5) / 100
        suma += cost

    return suma
n = int(input())
a = list(map(int, input().split()))
print(f"{f(a):.2f}")

