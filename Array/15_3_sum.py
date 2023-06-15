class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        two pointer solution
        one for loop start from 0 and left pointer = i+1, right pointer= right
        find the sum of the three numbers
        # time complexity: O(N^2)
        # space complexity: O(N)
        """
        if not nums:
            return []
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        use a hashset to store already seen numbers
        '''
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: list[int], i: int, res: list[list[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1