//https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/?envType=problem-list-v2&envId=recursion

class Solution {
    public:
        char kthCharacter(int k, string word = "a") {
            if (word.length() >= k){
                return word[k - 1];
            }else{
                word += f(k, word);
                return kthCharacter(k, word);
            }
        }

        string f(int k, string word, string alf = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"){
            string word_0 = "";
            for (int i = 0; i < word.length(); i++){
                auto it = find(alf.begin(), alf.end(), word[i]);
                int ind = it - alf.begin();
                word_0 += alf[ind + 1];
            }
            return word_0;
        }
};
