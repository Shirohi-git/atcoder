n, k = map(int, input().split())
h = sorted(map(int, input().split()))[::-1]

print(sum(h[k:]))
