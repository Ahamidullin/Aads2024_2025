def solve():
    import sys

    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    x.sort()

    S = [0] * (n + 1)
    for i in range(n):
        S[i + 1] = S[i] + x[i]

    q = int(sys.stdin.readline())
    answers = []

    def total_cost(i, a, b):
        left_count = i + 1
        left_sum = S[i + 1]
        right_count = n - left_count
        right_sum = S[n] - left_sum
        cost_left = a * (left_count * x[i] - left_sum)
        cost_right = b * (right_sum - right_count * x[i])
        return cost_left + cost_right

    for _ in range(q):
        line = sys.stdin.readline().split()
        a, b = int(line[0]), int(line[1])

        k0 = (n * b) // (a + b)
        cand_indices = [k0 - 1, k0, k0 + 1]
        best = None
        for ci in cand_indices:
            if 0 <= ci < n:
                cval = total_cost(ci, a, b)
                if best is None or cval < best:
                    best = cval
        answers.append(best)
    print("\n".join(map(str, answers)))
solve()
