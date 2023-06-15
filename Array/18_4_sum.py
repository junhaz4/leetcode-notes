class Solution:
    def fourSum(self, nums:list[int], target: int) ->list[list[int]]:
        # time complexity: O(N^3)
        # space complexity: O(N)
        nums.sort()
        n = len(nums)
        res = []

        def two_sum(first, second):
            left = second + 1
            right = n - 1
            while left < right:
                cur_sum = nums[first] + nums[second] + nums[left] + nums[right]
                if cur_sum == target:
                    res.append([nums[first], nums[second], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum > target:
                    right -= 1
                else:
                    left += 1

        for i in range(n - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                two_sum(i, j)
        return res


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                l= j+1
                r = n-1
                while l < r:
                    if nums[i]+nums[j]+nums[l]+nums[r]<target:
                        l += 1
                    elif nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r -= 1
                    else:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l]==nums[l+1]:
                            l += 1
                        while l < r and nums[r]==nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return result