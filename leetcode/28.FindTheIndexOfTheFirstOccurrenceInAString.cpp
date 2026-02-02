// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

#include <string>
#include <vector>

using namespace std;
class Solution {
public:
    int strStr(string s, string pre) {
        string t = pre + "#" + s;
        int n = t.size();
        vector<int> p(n, 0);
        
        for (int i = 1; i < n; i++) {
            int j = p[i - 1];
            
            while (j > 0 && t[i] != t[j]) {
                j = p[j - 1];
            }
            
            if (t[i] == t[j]) {
                j++;
            }
            p[i] = j;
            
            if (p[i] == pre.size()) {
                return i - 2 * pre.size();
            }
        }
        
        return -1;
    }
};
