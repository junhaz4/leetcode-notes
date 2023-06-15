class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        use hashmap to store the values and their indices {key: value}={number: index}
        time complexity: O(n)
        space complexity: O(n)
        '''
        hash_map = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in hash_map:
                return [i, hash_map[remain]]
            else:
                hash_map[nums[i]] = i
        return [-1,-1]

# brute force
# time complexity: O(n^2)
# space complexity: O(1)
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return [-1,-1]
