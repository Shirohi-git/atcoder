#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define all(v) v.begin(), v.end()
#define min_itr(v) *min_element(v.begin(), v.end())
#define max_itr(v) *max_element(v.begin(), v.end())
#define sum(v) accumulate(v.begin(), v.end(), 0LL)
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define for_itr(id, itr) for (auto& id : itr)
#define for_dic(key, val, dic) for (const auto& [key, val] : dic)
#define deg_to_rad(deg) (((deg) / 360) * 2 * M_PI)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define coutdeci cout << fixed << setprecision(15)

//隣接リスト push_backすると参照壊れるから中身だけコピペ
int nearlist(const matll& lst, matll& near) {
    for_itr(id, lst) {
        near[id[0] - 1].push_back(id[1] - 1);
        near[id[1] - 1].push_back(id[0] - 1);
    }
    return 0;
}

//幅優先探索
int bfs(const int& s, const matll& near, vector<ll>& res) {
    res[s] = 0;
    deque<ll> que;
    que.push_back(s);
    while (!que.empty()) {
        ll q;
        q = que.front();
        que.pop_front();
        for_itr(id, near[q]) {
            if (res[id] > -1) continue;
            res[id] = res[q] + 1;
            que.push_back(id);
        }
    }
    return 0;
}

//ダイクストラ法
int dijkstra(const int& s, const vector<matll>& w_near, vector<ll>& dist) {
    dist[s] = 0;
    priority_queue<vector<ll>> que;
    que.push({0, s});
    while (que.size() > 0) {
        ll d = que.top()[0], q = que.top()[1];
        que.pop();
        if (dist[q] < -d) continue;
        for_itr(nq, w_near[q]) {
            ll nxt = nq[0], tmp = -d + nq[1];
            if (dist[nxt] > tmp) {
                dist[nxt] = tmp;
                que.push({-tmp, nxt});
            }
        }
    }
    return 0;
}

// Unionfind
class Unionfind {
   private:
    vector<ll> res;
    map<ll, vector<ll>> group;

   public:
    ll N;
    vector<ll> parents;

    Unionfind(ll n0) {
        N = n0;
        parents = vector<ll>(N, -1);
    }

    ll find(ll x) {
        if (parents[x] < 0)
            return x;
        else {
            parents[x] = find(parents[x]);
            return parents[x];
        }
    }

    void unite(ll x, ll y) {
        x = find(x), y = find(y);
        if (x == y) return;
        if (parents[x] > parents[y]) {
            ll tmp = x;
            x = y, y = tmp;
        }
        parents[x] += parents[y];
        parents[y] = x;
    }

    bool same(ll x, ll y) { return (find(x) == find(y)); }

    ll roots_cnt() {
        ll cnt = 0;
        for_itr(pi, parents) if (pi < 0) cnt++;
        return cnt;
    }

    vector<ll>& roots() {
        res = vector<ll>(0);
        rep(i, N) if (parents[i] < 0) res.push_back(i);
        return res;
    }

    ll size(ll x) { return -parents[find(x)]; }

    vector<ll>& all_sizes() {
        res = vector<ll>(0);
        for_itr(pi, parents) if (pi < 0) res.push_back(-pi);
        return res;
    }

    vector<ll>& member(ll x) {
        res = vector<ll>(0);
        ll root = find(x);
        rep(i, N) if (find(i) == root) res.push_back(i);
        return res;
    }

    map<ll, vector<ll>>& all_members() {
        group = {};
        rep(i, N) if (parents[i] < 0) group[i] = vector<ll>(0);
        rep(i, N) group[find(i)].push_back(i);
        return group;
    }
};

// 強連結成分分解 rv_near: 逆向き枝, order: 帰りがけ順
class Strongly_Conected_Component {
   private:
    ll n;
    vector<ll> order, flag_dfs, flag_rdfs;
    matll near, nm_near, rv_near;

   public:
    ll cnt = 0;
    vector<ll> idx;

    Strongly_Conected_Component(ll n0, matll near0) {
        n = n0;
        near = near0;
        nm_near = near0;
        rv_near = matll(n, vector<ll>(0));
        rep(i, n) for_itr(j, near0[i]) rv_near[j].push_back(i);

        flag_dfs = vector<ll>(n, 0), order = vector<ll>(0);
        rep(i, n) if (!flag_dfs[i]) dfs(i);

        reverse(all(order));
        flag_rdfs = vector<ll>(n, 0), idx = vector<ll>(n, -1);
        for_itr(i, order) if (!flag_rdfs[i]) rdfs(i, cnt), cnt++;
    }

    void dfs(ll v) {
        flag_dfs[v] = 1;
        vector<ll> stack = {v};

        while (!stack.empty()) {
            ll now = stack.back();
            if (nm_near[now].empty()) {
                stack.pop_back();
                order.push_back(now);
            }
            while (!nm_near[now].empty()) {
                ll nxt = nm_near[now].back();
                nm_near[now].pop_back();
                if (!flag_dfs[nxt]) {
                    flag_dfs[nxt] = 1;
                    stack.push_back(nxt);
                    break;
                }
            }
        }
        return;
    }

    void rdfs(ll v, ll c) {
        idx[v] = c;
        vector<ll> stack = {v};

        while (!stack.empty()) {
            ll now = stack.back();
            stack.pop_back();
            if (flag_rdfs[now]) continue;
            flag_rdfs[now] = 1;
            for_itr(nxt, rv_near[now]) if (!flag_rdfs[nxt]) {
                idx[nxt] = c;
                stack.push_back(nxt);
            }
        }
        return;
    }
    // グラフ縮約
    matll construct() {
        matll graph(cnt, vector<ll>(0));
        rep(v, n) {
            ll v_id = idx[v];
            for_itr(w, near[v]) {
                ll w_id = idx[w];
                if (v_id != w_id) graph[v_id].push_back(w_id);
            }
        }
        return graph;
    }
};

int main() {
    ll n;
    cin >> n;

    return 0;
}
