#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int64_t S, int64_t T, int M, const std::vector<int64_t> &u, const std::vector<int64_t> &v) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t S, T;
    int M;
    std::cin >> S >> T >> M;
    std::vector<int64_t> u(M), v(M);
    REP (i, M) {
        std::cin >> u[i] >> v[i];
    }
    auto ans = solve(S, T, M, u, v);
    // failed to analyze output format
    // TODO: edit here
    std::cout << ans << '\n';
    return 0;
}
