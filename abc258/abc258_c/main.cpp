#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int64_t a, int b, const std::vector<std::string> &c, const std::vector<int64_t> &d, int64_t e) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t a;
    int b;
    int64_t e;
    std::cin >> a >> b;
    std::vector<std::string> c(b);
    std::vector<int64_t> d(b);
    REP (i, b) {
        std::cin >> c[i] >> d[i];
    }
    std::cin >> e;
    auto ans = solve(a, b, c, d, e);
    // failed to analyze output format
    // TODO: edit here
    std::cout << ans << '\n';
    return 0;
}
