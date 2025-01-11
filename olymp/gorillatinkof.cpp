#include <iostream>
#include <vector>


std::vector<int> f(int n) {
    if (n == 2){
        return std::vector<int>{-1};
    }int i = 2;
    while (i * i <= n){
        if (n % i == 0) {
            int x = n / i;
            int y = i;
            return std::vector<int>{y, x};
        }
        i++;
    }
    return std::vector<int>{-1};
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::vector<int> result = f(n * n + 1);
        if (result.size() == 1){
            std::cout << result[0];
        }else{
            std::cout << result[0] << " " << result[1];
        }
        std::cout << std::endl;
    }
    return 0;
}