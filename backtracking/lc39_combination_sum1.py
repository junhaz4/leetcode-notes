class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []
        def backtracking(candidates,target,startIndex):
            if target==0:
                result.append(path[:])
                return 
            if target < 0:
                return 
            for i in range(startIndex,len(candidates)):
                path.append(candidates[i])
                target -= candidates[i]
                backtracking(candidates,target,i)
                target += candidates[i]
                path.pop()
        backtracking(candidates,target,0)
        
        def backtrack(candidates,target,startIndex,curSum):
            if target==curSum:
                result.append(path[:])
                return 
            if target < curSum:
                return 
            for i in range(startIndex,len(candidates)):
                path.append(candidates[i])
                curSum += candidates[i]
                backtrack(candidates,target,i,curSum)
                curSum -= candidates[i]
                path.pop()
        backtrack(candidates,target,0,0)
        
        #剪枝 如果本层sum + condidates[i] > target，就提前结束遍历，剪枝
        def backtrack2(candidates,target,startIndex,curSum):
            if target==curSum:
                result.append(path[:])
                return 
            for i in range(startIndex,len(candidates)):
                if curSum + candidates[i]>target:
                    return
                path.append(candidates[i])
                curSum += candidates[i]
                backtrack2(candidates,target,i,curSum)
                curSum -= candidates[i]
                path.pop()
        candidates.sort()
        backtrack2(candidates,target,0,0)
        return result
    
'''
class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(vector<int>& candidates,int target,int sum, int startIndex){
        if (sum==target){
            result.push_back(path);
            return;
        }
        for(int i=startIndex; i<candidates.size() && sum+candidates[i]<=target;i++){
            sum+=candidates[i];
            path.push_back(candidates[i]);
            backtracking(candidates,target,sum,i);
            sum-= candidates[i];
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        backtracking(candidates,target,0,0);
        return result;
    }
};
'''