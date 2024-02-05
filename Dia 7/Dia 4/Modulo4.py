def pares(T_n, k):
    pairs = set()

    n = len(T_n)

    for i in range(n):
        for j in range(i + 1, n):
            if (T_n[i] + T_n[j]) % k == 0:
                pairs.add((T_n[i], T_n[j]))

    return pairs
