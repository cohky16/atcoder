#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


std::string solve(auto N, const std::vector<std::vector<auto> > &A) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    auto N;
    std::cin >> N;
    std::vector<std::vector<auto> > A(2 * N + 4, std::vector<auto>((2 * N + 4)));
    REP (j, N + 4) {
        REP (i, N) {
            std::cin >> A[i + j][i + j];
        }
    }
    auto ans = solve(N, A);
    std::cout << ans << '\n';
    return 0;
}
