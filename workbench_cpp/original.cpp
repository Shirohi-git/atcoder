#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define all(v) v.begin(), v.end()
#define min_itr(v) *min_element(v.begin(), v.end())
#define max_itr(v) *max_element(v.begin(), v.end())
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define for_itr(id, itr) for (auto& id : itr)
#define for_dic(key, val, dic) for (const auto& [key, val] : dic)

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    rep(i, n) { cin >> a[i]; }

    return 0;
}