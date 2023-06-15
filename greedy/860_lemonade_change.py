class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        '''
        局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零
        '''
        # time O(N) space O(1)
        if bills[0] != 5:
            return False
        five = 0
        ten = 0
        twenty = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
        return True