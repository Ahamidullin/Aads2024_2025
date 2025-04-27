#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    string name;
    cin >> name;
    int M = (int)name.size();

    vector<string> cube(N);
    for (int i = 0; i < N; ++i) cin >> cube[i];
    vector<vector<int>> g(N);
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            if (cube[i].find(name[j]) != string::npos) g[i].push_back(j);

    vector<int> match_pos(M, -1);
    function<bool(int, vector<int>&)> dfs = [&](int v, vector<int>& used) -> bool {
        if (used[v]) return false;
        used[v] = 1;
        for (int p : g[v]) {
            if (match_pos[p] == -1 || dfs(match_pos[p], used)) {
                match_pos[p] = v;
                return true;
            }
        }
        return false;
    };

    int matched = 0;
    for (int v = 0; v < N && matched < M; ++v) {
        vector<int> used(N, 0);
        if (dfs(v, used)) ++matched;
    }

    if (matched < M) {
        cout << "NO\n";
        return 0;
    }

    vector<int> cube_for_pos(M);
    for (int p = 0; p < M; ++p) cube_for_pos[p] = match_pos[p] + 1;

    cout << "YES\n";
    for (int i = 0; i < M; ++i) {
        cout << cube_for_pos[i] << (i + 1 == M ? '\n' : ' ');
    }
    return 0;
}
