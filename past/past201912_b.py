n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(1,n):
    if a[i] < a[i-1]:
        print('down', a[i-1] - a[i])
    elif a[i] > a[i-1]:
        print('up', a[i] - a[i-1])
    else:
        print('stay')
