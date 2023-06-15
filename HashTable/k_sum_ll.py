import collections
'''
divide k arrays into two groups. For the first group, we will have k/2 nested loops to count sums. 
Another k/2 nested loops will enumerate arrays in the second group and search for complements.

The first group will be processed by addToHash recursive function, which accumulates sum and 
terminates when adding the final sum to a hashmap m

The second function, countComplements, will process the other group, accumulating the complement value. 
In the end, it searches for the final complement value in the hashmap and adds its count to the result.

time complexity: O(n^(k/2)) will have k/2 nested loops to count sums. Another k/2 nested loops to search for complements.
if the number is odd, then O(n*((k+1)/2))
space complexity: O(n^(k/2)) for hashmap
'''
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4, numsk):
        map = collections.defaultdict(int)
        lists =[nums1, nums2, nums3, nums4, numsk] # put k lists into a list
        def nsumCount():
            add_to_hash(0,0)
            return count_complement(len(lists)//2,0)

        def add_to_hash(i, total):
            if i == len(lists)//2:
                map[total] += 1
            else:
                for n in lists[i]:
                    add_to_hash(i+1, total+n)

        def count_complement(i,complement):
            if i == len(lists):
                return map[complement]
            count = 0
            for n in lists[i]:
                count += count_complement(i+1, complement-n)
            return count
        return nsumCount()