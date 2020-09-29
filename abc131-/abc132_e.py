from collections import deque


def nearlist(N):
    NEAR = [set() for _ in range(3 * N)]
    for a, b in uv:
        a, b = 3 * (a - 1), 3 * (b - 1)
        NEAR[a].add(b + 1)
        NEAR[a + 1].add(b + 2)
        NEAR[a + 2].add(b)
    return NEAR


def bfs(S, T, N):
    S, T = 3 * (S - 1), 3 * (T - 1)
    dist, flag = [-3] * (3 * N), [0] * (3 * N)
    dist[S], flag[S] = 0, 1
    que = deque([S])

    while que:
        q = que.popleft()
        for i in near[q]:
            if flag[i]:
                continue
            dist[i], flag[i] = dist[q] + 1, 1
            que.append(i)
    return dist[T] // 3


n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# 解説AC
near = nearlist(n)
print(bfs(s, t, n))
