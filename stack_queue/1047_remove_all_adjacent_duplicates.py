class Solution:
    def removeDuplicates(self, s: str) -> str:
        # method 1: using stack
        # time complexity: O(N) N: length of s
        # space complexity: O(N-D) D: length of total duplicates
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # method 2: using two pointers
        # time complexity: O(N) N: length of s
        # space complexity: O(N)
        fast, slow = 0, 0
        res = list(s)
        while fast < len(res):
            res[slow] = res[fast]
            if slow > 0 and res[slow] == res[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[:slow])