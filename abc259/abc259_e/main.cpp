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
int64_t solve(int a, const std::vector<int64_t> &b, const std::vector<std::vector<int64_t> > &c, const std::vector<std::vector<int64_t> > &d) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int a;
    std::cin >> a;
    std::vector<int64_t> b(a);
    std::vector<std::vector<int64_t> > c(a, std::vector<int64_t>((b_i))), d(a, std::vector<int64_t>((b_i)));
    REP (i, a) {
        std::cin >> b[i];
        REP (j, b_i) {
            std::cin >> c[i][j] >> d[i][j];
        }
    }
    auto ans = solve(a, b, c, d);
    std::cout << ans << '\n';
    return 0;
}
