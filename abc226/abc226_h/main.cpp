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
int64_t solve(int N, int64_t K, const std::vector<int64_t> &L, const std::vector<int64_t> &R) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N;
    int64_t K;
    std::cin >> N;
    std::vector<int64_t> L(N), R(N);
    std::cin >> K;
    REP (i, N) {
        std::cin >> L[i] >> R[i];
    }
    auto ans = solve(N, K, L, R);
    std::cout << ans << '\n';
    return 0;
}
