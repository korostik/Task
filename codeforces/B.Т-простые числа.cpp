//https://codeforces.com/contest/230/problem/B

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
bool proct(int n){
    if (n == 1)return false;
    for (int i = 2; i < sqrt(n) + 1; i++){
        if (n % i == 0)return false;
    }
    return true;
}
 
void solve(vector <long long int> a){
    for (int i = 0; i < a.size(); i++){
        if (a[i] == 4)cout << "YES" << endl;
        else{
            if (a[i] % 2 == 1){
                if (sqrt(a[i]) == int(sqrt(a[i]))){
                    if (proct(sqrt(a[i]))){
                        cout << "YES"<< endl;
                    }else{
                        cout << "NO"<< endl;
                    }
                }else{cout << "NO"<< endl;}
                    
            }else{cout << "NO"<< endl;}
        }
    }
}
 
int main(){
    int t;
    cin >> t;
    vector <long long int> a(t);
    for (int i = 0; i < t; i++){
        cin >> a[i];
    }
    solve(a);
}
