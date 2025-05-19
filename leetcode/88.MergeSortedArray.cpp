// https://leetcode.com/problems/merge-sorted-array/description/
#include <algorithm>
class Binary {
public:
    int search(vector <int> a, int x) {
        int l = 0;
        int r = a.size() - 1;
        while (l <= r){
            int mid = (l + r) / 2;
            if (a[mid] == x){return mid;}
            else if(x < a[mid]){r = mid - 1;}
            else{l = mid + 1;}
        }
        return l;
    }
};

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        Binary objb;
        nums1.resize(m);
        for (auto x : nums2){
            int ind = objb.search(nums1, x);
            nums1.insert(nums1.begin() + ind, x);
        }
    }
};
