class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # time complexity: O(n)
        # space complexity: O(n) no extra space used
        hash_set = set(nums1)
        res = set()
        for n in nums2:
            if n in hash_set:
                res.add(n)
        return list(res)

# Follow-up: solve it under O(n) time and O(1) space and lists are sorted
# Cases to take into consideration include: duplicates, negative values, single value lists, 0's, and empty list arguments.
def intersection(nums1, nums2):
    # if the lists are already sorted and you're told to solve in O(n) time and O(1) space:
    nums1.sort()  # assume sorted
    nums2.sort()  # assume sorted

    # iterate both nums backwards till at least 1 is empty
    # if num2[j] > num1[i], pop num2
    # if num2[j] < num1[i], pop num1
    # if equal and num not last appended to result, append to result and pop both nums
    result = []
    while nums1 and nums2:
        if nums1[-1] > nums2[-1]:
            nums1.pop()
        elif nums1[-1] < nums2[-1]:
            nums2.pop()
        else: # to avoid duplicates
            if result == [] or nums1[-1] != result[-1]:
                result.append(nums1[-1])
            nums1.pop()
            nums2.pop()
    return result

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        l1, l2 = len(nums1)-1, len(nums2)-1
        result = []
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] > nums2[l2]:
                l1 -= 1
            elif nums1[l1] < nums2[l2]:
                l2 -= 1
            else:
                if result == [] or result[-1] != nums1[l1]:
                    result.append(nums1[l1])
                l1 -= 1
                l2 -= 1
        return result

