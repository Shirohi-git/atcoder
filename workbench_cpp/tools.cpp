#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define all(v) v.begin(), v.end()
#define min_val(v) *min_element(v.begin(), v.end())
#define max_val(v) *max_element(v.begin(), v.end())
#define max_idx(v) distance(v.begin(), max_element(v.begin(), v.end()))
#define sum(v) accumulate(v.begin(), v.end(), 0LL)
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += s)
#define repdic(key, val, dic) for (const auto& [key, val] : dic)
#define deg_to_rad(deg) (((deg) / 360) * 2 * M_PI)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define coutdeci cout << fixed << setprecision(15)

//二分探索判定
bool isOK(ll mid) {
    bool res;
    if (res)
        return true;
    else
        return false;
}

//二分探索
int binary_search(ll l, ll r) {
    ll left = l, right = r + 1;
    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (isOK(mid))
            right = mid;
        else
            left = mid;
    }
    return left;
}

//累乗(mod)
ll mod_pow(ll x, ll y, const ll& mod) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res = (res * x) % mod;
        x = (x * x) % mod;
        y >>= 1;
    }
    return res;
}

//組合せ数
class Combination {
   private:
    vector<ll> fact, inv, factinv;

   public:
    ll N, MOD;

    Combination(ll n0, ll mod) {
        N = n0, MOD = mod;
        fact = vector<ll>(N + 1, -1);
        inv = vector<ll>(N + 1, -1);
        factinv = vector<ll>(N + 1, -1);

        fact[0] = 1, fact[1] = 1;
        inv[0] = 0, inv[1] = 1;
        factinv[0] = 1, factinv[1] = 1;
        repr(i, 2, N + 1) {
            fact[i] = (fact[i - 1] * i) % MOD;
            inv[i] = mod_pow(i, MOD - 2, MOD);
            factinv[i] = (factinv[i - 1] * inv[i]) % MOD;
        }
    }

    ll count(ll cn, ll cr) {
        if ((cr < 0) || (cn < cr)) return 0;
        cr = min(cr, cn - cr);
        ll res = fact[cn] * factinv[cr] % MOD;
        res = res * factinv[cn - cr] % MOD;
        return (res % MOD + MOD) % MOD;
    }
};

// Fenwicktree(BinaryIndexedTree) 0-indexed
class Fenwicktree {
   private:
    vector<ll> tree;

   public:
    ll N;
    Fenwicktree(int n0) {
        N = n0;
        tree = vector<ll>(N, 0);
    }

    // RSQ[0,r]
    ll accsum(int r) {
        ll res = 0;
        r++;
        while (r > 0) {
            res += tree[r - 1];
            r -= r & -r;
        }
        return res;
    }

    // update vec[idx] += x
    void update(ll idx, ll x) {
        idx++;
        while (idx <= N) {
            tree[idx - 1] += x;
            idx += idx & -idx;
        }
        return;
    }

    // RSQ[l,r)
    ll query(ll l, ll r) { return accsum(r - 1) - accsum(l - 1); }
};

//行列積
int mat_product(matll a, matll b, matll& res) {
    ll n = a.size(), m = b.size(), l = b[0].size();
    if (m != a[0].size()) {
        cout << "can't\n";
        return 0;
    }
    rep(i, n) rep(j, l) rep(k, m) { res[i][j] += a[i][k] * b[k][j]; }
    return 0;
}

//行列累乗 res[i] = mat**(2**i)
int mat_powlst(ll cnt, matll mat, vector<matll>& res) {
    res[0] = mat;
    rep(p, cnt) mat_product(res[p], res[p], res[p + 1]);
    return 0;
}

int main() {
    ll n;
    cin >> n;

    return 0;
}
