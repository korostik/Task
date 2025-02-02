#include <iostream>
#include <vector>


std::vector<int> f(int n) {
    if (n == 2){
        return std::vector<int>{-1};
    }int i = 2;
<<<<<<< HEAD
    while (i * i <= n){
        if (n % i == 0) {
=======
    while (i * i <= n){ 
        if (n % i == 0)  {
>>>>>>> edaa3b3c7dd59f889af9d5db447ae82f563b4a18
            return std::vector<int>{i, n / i};
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

