class Solution:
    def combinationSum2(self, candidates:list[int], target: int) ->list[list[int]]:
        # Method 1 use extra array to check if repeating elements used in previous step
        '''
        要去重的是“同一树层上的使用过”，如果判断同一树层上元素（相同的元素）是否使用过
        如果candidates[i] == candidates[i - 1] 并且 used[i - 1] == false 就说明前一个树枝使用了candidates[i - 1]
        也就是说同一树层使用过candidates[i - 1],此时for循环里就应该做continue的操作。
        在candidates[i] == candidates[i - 1]相同的情况下：
        used[i - 1] == true 说明同一树枝candidates[i - 1]使用过
        used[i - 1] == false 说明同一树层candidates[i - 1]使用过
                                    used[0,0,0]
                                    [1,1,2]中取一
                                   /     |       \
                             [1,0,0]  [0,1,0]    [0,0,1]
                              [1]      同一树层重复
                             [1,2]取一  元素不可重复选取
                            /     \
                         [1,1,0]  [1,0,1]
                         [1,1]     [1,1]
                         [2]取一    []取一
                         同一树枝同一元素可重复选 
        '''
        self.result = []
        self.path = []
        self.used = [False]*len(candidates)
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        def backtracking(candidates,target,curSum,startIndex):
            if curSum == target:
                self.result.append(self.path[:])
                return 
            for i in range(startIndex,len(candidates)):
                # 剪枝，同39.组合总和
                if curSum+candidates[i]>target:
                    return
                # 要对同一树层使用过的元素进行跳过
                if i > 0 and candidates[i]==candidates[i-1] and self.used[i-1]==False:
                    continue
                curSum += candidates[i]
                self.path.append(candidates[i])
                self.used[i] = True
                backtracking(candidates,target,curSum,i+1)
                self.used[i] = False
                curSum -= candidates[i]
                self.path.pop()
        backtracking(candidates,target,0,0)
        return self.result 
    
        # Method 2
        self.result = []
        self.path = []
        candidates.sort()
        def backtracking2(candidates,target,curSum,startIndex):
            if curSum == target:
                self.result.append(self.path[:])
                return 
            for i in range(startIndex,len(candidates)):
                if curSum+candidates[i]>target:
                    return 
                if i>startIndex and candidates[i]==candidates[i-1]:
                    continue
                curSum += candidates[i]
                self.path.append(candidates[i])
                backtracking2(candidates,target,curSum,i+1)
                curSum -= candidates[i]
                self.path.pop()    
        backtracking2(candidates,target,0,0)
        return self.result