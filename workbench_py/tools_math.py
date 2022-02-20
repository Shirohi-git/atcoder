# pypyは文字列結合NG,再帰NG

# floatを使うときは大きい数に注意
# if in dict.values() はO(n)

# 入力が多い時
import sys
input = sys.stdin.readline

# 再帰の深さに注意
import sys
sys.setrecursionlimit(10 ** 7)

# 冪乗 n ** m % mod == pow(n, m, mod)
# フェルマーの小定理(pは素数, aはpと互いに素)
# pow(a, p-1, p) == 1 (mod_p) <=> pow(a, p-2, p) == a**(-1) (mod_p)
# 割り算するところを掛け算できるので先にmodが取れる


def ceil(x, y):  # 天井関数 ceil(X/Y) (Y>1)
    return (x + y - 1) // y


def lcm(X, Y):  # 最小公倍数
    from math import gcd
    return (X * Y) // gcd(X, Y)


def quotient(x, y): # 有理数クラス(y/x)
    from math import gcd
    if x == y == 0:
        return (0, 0)
    if (y < 0) or (y == 0 and x < 0):
        x, y = -x, -y
    t = gcd(x, y)
    return (x//t, y//t)


def extgcd(a, b):  # 拡張互除法
    x, y, u, v = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x, u = u, x - q * u
        y, v = v, y - q * v
    return a, x, y


def factorize(N):  # 素因数分解
    p, PRIME = 2, []
    while p * p <= N:
        while N % p == 0:
            N //= p
            PRIME.append(p)
        p += 1
    if N > 1:
        PRIME.append(N)
    return PRIME


def makedivisor(n0):  # 約数列挙
    p, upper, lower = 1, [], []
    while p * p <= n0:
        if n0 % p == 0:
            lower.append(p)
            if p * p != n0:
                upper.append(n0 // p)
        p += 1
    return lower + upper[::-1]


def totient(N):  # オイラーのトーシェント関数
    p, phi = 2, N
    while p * p <= N:
        if N % p == 0:
            phi = phi // p * (p - 1)
        while N % p == 0:
            N //= p
        p += 1
    if N > 1:
        phi = phi // N * (N - 1)
    return phi


# エラトステネスの篩
class Eratosthenes():
    # 素数リスト生成 O(n*log(log n))
    def __init__(self, N):
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]

    # 高速素因数分解 O(log num)
    def factor(self, NUM):
        PRIME = set()
        while NUM > 1:
            PRIME.add(self.fact[NUM])
            NUM //= self.fact[NUM]
        return PRIME


# 立ってるbitの数リスト
def bitcount(N):
    bitcnt = [0]
    for _ in range(N):
        bitcnt += [i + 1 for i in bitcnt]
    return bitcnt


# bitの部分集合 sum(0~2^N) = O(3^N)
def bitsubset(num):
    ini = num
    res = [num]
    while num > 0:
        num = (num-1) & ini
        res.append(num)
    return res


# nCr(mod p) #n<=10**6
class Combination():
    # cmbの前処理(階乗, 各iの逆元, 階乗の逆元)
    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    # nCr(mod p) #前処理必要
    def count(self, N, R):
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        div = self.FACTINV[R] * self.FACTINV[N-R] % self.mod
        return self.FACT[N] * div % self.mod


# nCr(mod p) #n>=10**7,r<=10**6 #前処理不要
def bigcmb(N, R, MOD):
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact = (fact * (N - i + 1)) % MOD
        inv = (inv * i) % MOD
    return fact * pow(inv, MOD - 2, MOD) % MOD


# 行列積
def mat_product(a, b):
    n, m, l = len(a), len(b), len(b[0])
    res = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]
    return res


# 行列累乗 res[i] = mat**(2**i)
def mat_powlst(cnt, mat):
    n = len(mat)
    res = [[[0] * n for _ in range(n)] for _ in range(cnt+1)]
    res[0] = [[matij for matij in mati] for mati in mat]
    for i in range(cnt):
        res[i+1] = mat_product(res[i], res[i])
    return res


def rad_to_deg(rad):
    from math import pi as PI
    return (((rad) / 2 / PI) * 360)


# 偏角ソート
def arg_sort(points, ymax=10**20):
    
    def sub_sort(sub_p):
        if (not sub_p) or (sub_p[0][0] == 0):
            return sub_p
        res = sorted(sub_p, key=lambda p: p[1] * ymax // p[0])
        return res

    group = [[], [], [], [], []]
    for xi, yi in points:
        if yi < 0:
            group[2 + (xi >= 0) + (xi > 0)].append((xi, yi))
        elif yi >= 0:
            group[(xi <= 0) + (xi < 0)].append((xi, yi))

    res = sum([sub_sort(gi) for gi in group], [])
    return res


# 凸包
def convex_hull(point_lst):
    
    # 時計回りか # 一直線上で高々2点の場合 ">="
    def is_CW(ax, ay, bx, by, cx=0, cy=0):
        res = (bx-cx) * (ay-cy) - (by-cy) * (ax-cx)
        return res > 0

    # 半分凸包
    def half_hull(lst):
        res = []
        for pi in lst:
            while len(res) > 1 and is_CW(*pi, *res[-2], *res[-1]):
                res.pop()
            res.append(pi)
        return res

    point_lst = sorted(point_lst)
    res1 = half_hull(point_lst)
    res2 = half_hull(point_lst[::-1])
    return res1 + res2[1:]


# 畳み込み
def convolve(a, b):
    
    from math import pi as PI, cos, sin

    # 高速フーリエ変換 O(nlogn)
    def FFT(lst, inv=False):
        n = len(lst)
        num = (n-1).bit_length()

        res = lst[:]
        for i in range(n):
            j = 0
            for k in range(num):
                j |= ((i >> k) & 1) << (num - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(num):
            i = (1 << i)
            for j in range(i):
                x = (2*inv - 1) * (2*PI*j) / (2*i)
                w = complex(cos(x), sin(x))
                for k in range(0, n, i*2):
                    s, t = res[j+k], res[i+j+k] * w
                    res[j+k], res[i+j+k] = s+t, s-t
        if (inv):
            res = [ri / n for ri in res]
        return res

    len_ab = len(a) + len(b) - 1
    n = 1 << len_ab.bit_length()
    a += [0] * (n-len(a))
    b += [0] * (n-len(b))

    res = [ai * bi for ai, bi in zip(FFT(a), FFT(b))]
    res = [int(fi.real + 0.1) for fi in FFT(res, True)[:len_ab]]
    return res


# 畳み込み(MOD)
def convolve_MOD(a, b):
    mod = 998244353
    g, e = pow(3, 119, mod), 24
    ginv = pow(g, mod-2, mod)
    # 998244353 = 119 * 2**23 + 1

    # 高速剰余変換 O(nlogn)
    def FMT(lst, inv=False):
        res = lst[:]
        for i in range(n):
            j = 0
            for k in range(n_lenbit):
                j |= ((i >> k) & 1) << (n_lenbit - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(n_lenbit):
            w = 1
            wp = Winv[e-2-i] if inv else W[e-2-i]
            pow2i = (1 << i)
            
            for j in range(pow2i):
                for k in range(1 << (n_lenbit-i-1)):
                    idx = k * pow2i*2 + j
                    s, t = res[idx], res[idx + pow2i] * w
                    res[idx], res[idx + pow2i] = (s + t) % mod, (s - t) % mod
                w = (w * wp) % mod

        if (inv):
            n_inv = pow(n, mod-2, mod)
            res = [ri * n_inv % mod for ri in res]
        return res


    W, Winv = [g], [ginv]
    for _ in range(e):
        W.append(W[-1]**2 % mod)
        Winv.append(Winv[-1]**2 % mod)
    len_ab = len(a) + len(b) - 1
    n = 1 << len_ab.bit_length()
    n_lenbit = (n-1).bit_length()
    a += [0] * (n-len(a))
    b += [0] * (n-len(b))

    res = [ai * bi % mod for ai, bi in zip(FMT(a), FMT(b))]
    res = FMT(res, inv=True)[:len_ab]
    return res