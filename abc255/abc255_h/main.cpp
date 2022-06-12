#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

constexpr int64_t MOD = 998244353;
auto solve(int64_t N, int Q, const std::vector<int64_t> &D, const std::vector<int64_t> &L, const std::vector<int64_t> &R) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t N;
    int Q;
    std::cin >> N >> Q;
    std::vector<int64_t> D(Q), L(Q), R(Q);
    REP (i, Q) {
        std::cin >> D[i] >> L[i] >> R[i];
    }
    auto ans = solve(N, Q, D, L, R);
    REP (i, Q) {
        std::cout << a[i] << '\n';
    }
    return 0;
}
