from bisect import bisect


def main():
    a1, a2 = A[:N//2], A[N//2:]
    lst1 = [[] for _ in range(N+1)]
    for bit in range(1 << len(a1)):
        cost, cnt = 0, 0
        for i in range(len(a1)):
            cost += a1[i] * (bit & 1)
            cnt += (bit & 1)
            bit >>= 1
        lst1[cnt].append(cost)

    lst2 = [[] for _ in range(N+1)]
    for bit in range(1 << len(a2)):
        cost, cnt = 0, 0
        for i in range(len(a2)):
            cost += a2[i] * (bit & 1)
            cnt += (bit & 1)
            bit >>= 1
        lst2[cnt].append(cost)

    lst2 = [sorted(l2i) for l2i in lst2]
    ans = 0
    for i in range(N+1):
        if (K-i >= 0):
            ans += sum(bisect(lst2[K-i], P - y1) for y1 in lst1[i])
    return print(ans)


if __name__ == '__main__':
    N, K, P = map(int, input().split())
    A = list(map(int, input().split()))

    main()
