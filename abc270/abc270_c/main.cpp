#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int N, int64_t X, int64_t Y, const std::vector<int64_t> &U, const std::vector<int64_t> &V) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N;
    int64_t X, Y;
    std::cin >> N;
    std::vector<int64_t> U(N - 1), V(N - 1);
    std::cin >> X >> Y;
    REP (i, N - 1) {
        std::cin >> U[i] >> V[i];
    }
    auto ans = solve(N, X, Y, U, V);
    REP (i, X) {
        std::cout << a[i] << ' ' << d[i] << ' ';
    }
    std::cout << '\n';
    return 0;
}
