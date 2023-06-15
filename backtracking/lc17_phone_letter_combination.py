class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        letter_map = {"2":"abc",
                      "3":"def",
                      "4":"ghi",
                      "5":"jkl",
                      "6":"mno",
                      "7":"pqrs",
                      "8":"tuv",
                      "9":"wxyz",
                      "1":"#`*.,/\[]_-+=?><|~@$%^&()"}
        self.result = []
        self.s = ""
        # index is used to indicate which digit in given digits will traversal 
        def backtracking(digits,index):
            if index == len(digits):
                self.result.append(self.s)
                return 
            digit = digits[index]
            letters = letter_map[digit]
            for letter in letters:
                self.s +=letter
                backtracking(digits,index+1)
                self.s = self.s[:-1]
        backtracking(digits,0)
        return self.result


'''
class Solution {
private:
    const string letterMap[10] = {
        "", // 0
        "", // 1
        "abc", // 2
        "def", // 3
        "ghi", // 4
        "jkl", // 5
        "mno", // 6
        "pqrs", // 7
        "tuv", // 8
        "wxyz", // 9
    };
public:
    vector<string> result;
    string s;
    void backtracking(const string&digits, int index){
        if (index==digits.size()){
            result.push_back(s);
            return;
        }
        int digit = digits[index]-'0';
        string letters = letterMap[digit];
        for (int i=0; i<letters.size();i++) {
            s.push_back(letters[i]);
            backtracking(digits,index+1);
            s.pop_back();
        } 
    }
    vector<string> letterCombinations(string digits) {
        if (digits.size()==0){
            return result; 
        }
        backtracking(digits,0);
        return result;
    }
};
'''