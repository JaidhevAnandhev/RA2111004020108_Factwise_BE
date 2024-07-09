def maximum_Score(C, K):
    best = total = sum(C[:K])
    for i in range(K - 1, -1, -1):
        total += C[i + len(C) - K] - C[i]
        best = max(best, total)
    return best


print(maximum_Score([1, 2, 3, 4, 5, 6, 1], 3))
