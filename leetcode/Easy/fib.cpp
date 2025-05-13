//https://leetcode.com/problems/fibonacci-number/description/?envType=problem-list-v2&envId=recursion

class Solution {
    public:
        int fib(int n) {
            if (n < 2){return n;}
            return fib(n - 1) + fib(n - 2);
        }
    };
