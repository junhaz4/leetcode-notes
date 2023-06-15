class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1: fixed length hash table
        record = [0]*26
        for i in range(len(s)):
            record[ord(s[i])-ord('a')] += 1
        for i in range(len(t)):
            record[ord(t[i])-ord('a')] -= 1
        for i in record:
            if i != 0:
                return False
        return True
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 2: variable length hash table
        count = Counter(s)
        for char in t:
            if char not in count:
                return False
            else:
                count[char] -= 1
        for char in count:
            if count[char] != 0:
                return False
        return True