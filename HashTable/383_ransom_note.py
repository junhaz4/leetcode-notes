class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        fixed length hashmap, store the frequency of each character in the magazine and try to match it in the ransomNote.
        time complexity: o(m)
        space complexity: O(1)
        '''
        char = [0]*26
        for c in magazine:
            char[ord(c)-ord('a')] += 1
        for c in ransomNote:
            if char[ord(c)-ord('a')] == 0:
                return False
            else:
                char[ord(c)-ord('a')] -= 1
        return True
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        variable length hashmap
        time complexity: O(m)
        space complexity: O(1)
        '''
        from collections import defaultdict
        hashmap = defaultdict(int)
        for x in magazine:
            hashmap[x] += 1

        for x in ransomNote:
            value = hashmap.get(x)
            if value is None or value <= 0:
                return False
            else:
                hashmap[x] -= 1
        return True


class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        # use a dict to store the number of letter occurance in ransomNote
        hashmap = dict()
        for s in ransomNote:
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1

        # check if the letter we need can be found in magazine
        for l in magazine:
            if l in hashmap:
                hashmap[l] -= 1

        for key in hashmap:
            if hashmap[key] > 0:
                return False

        return True

import collections
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
    magazine_counts = collections.Counter(magazine)
    ransom_note_counts = collections.Counter(ransomNote)

    # For each *unique* character in the ransom note:
    for char, count in ransom_note_counts.items():
        # Check that the count of char in the magazine is equal
        # or higher than the count in the ransom note.
        magazine_count = magazine_counts[char]
        if magazine_count < count:
            return False

    # If we got this far, we can successfully build the note.
    return True