# Method 1 use library
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        res = []
        for i in range(len(s)-1,-1,-1):
            if s[i] != '':
                res.append(s[i])
        return ' '.join(res)

# Method 2 use deque
# O(N) space, o(N) time
from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < right and s[right] == ' ':
            right -= 1
        while left < right and s[left] == ' ':
            left += 1
        que = deque()
        word = []
        while left <= right:
            # reach the empty space and all elements before form a word
            if s[left] == " " and word:
                que.appendleft(''.join(word))
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        que.appendleft(''.join(word)) # add the last word
        return ' '.join(que)


class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        1. remove extra space
        2. reverse the whole string
        3. reverse each word
        time complexity: O(n)
        space: O(1) no extra memory used
        '''
        def trim_space(s):
            left, right = 0, len(s)-1
            while left < right and s[left] == ' ':
                left += 1
            while left < right and s[right] == ' ':
                right -= 1
            chars = []
            while left <= right:
                if s[left] != " ":
                    chars.append(s[left])
                elif chars[-1] != " ":
                    chars.append(s[left])
                left += 1
            return chars

        def reverse_string(s, left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return None

        def reverse_word(s):
            n = len(s)
            left, right = 0, 0
            while left < n:
                while right < n and s[right] != " ":
                    right += 1
                reverse_string(s, left, right-1)
                right += 1
                left = right
            return None

        new_s = trim_space(s)
        reverse_string(new_s, 0, len(new_s) - 1)
        reverse_word(new_s)
        return ''.join(new_s)
