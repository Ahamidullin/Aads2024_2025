#include<iostream>
#include<vector>

std::vector<int> used;
std::vector<std::vector<size_t> > left;
std::vector<size_t> right;

bool dfs(size_t v) {
    used[v] = true;
    for (const size_t to : left[v]) {
        if (right[to] == 0) {
            right[to] = v;
            return true;
        }
    }
    for (const size_t to : left[v]) {
        if (!used[right[to]] && dfs(right[to])) {
            right[to] = v;
            return true;
        }
    }
    return false;
}

int main() {
    size_t n = 0, m = 0;
    std::cin >> n >> m;
    ++n;
    ++m;
    left.resize(n);
    right.resize(m);
    for (size_t v = 1; v < n; ++v) {
        while(true) {
            size_t x = 0;
            std::cin >> x;
            if (x == 0) break;
            left[v].push_back(x);
        }
    }
    used.assign(n, false);
    int cnt = 0;
    for (size_t v = 1; v < n; ++v) {
        if (dfs(v)) {
            ++cnt;
            used.assign(n, false);
        }
    }
    std::cout << cnt << '\n';

    for (int v = 0; v < m; ++v) {
        if (right[v] != 0) {
            std::cout << right[v] << ' ' << v << '\n';
        }
    }


    return 0;
}