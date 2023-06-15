class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        sliding window of fixed size len(words), keep track of all the words in a HashMap and try to match them in the given string.
        1. keep track the frequency of every word in a hashmap
        2. start from each index and try to match all words
        3. In each iteration, keep track of all the words that we have already seen in another HashMap.
        4. If a word is not found or has a higher frequency than required, we can move on to the next character in the string.
        5. store the index if we could match all words
        # time complexity: O(N*M*Len) M=len(words),N=len(s),len = length of each word
        # space complexity: O(M+N)
        """
        if not s or not words:
            return []
        # store the frequency of required words in a hashmap
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        word_count = len(words)
        word_length = len(words[0])
        sub_size = word_length * word_count
        n = len(s)
        # iterate through the s to find all the substrings that match the word_freq
        res = []
        for i in range(0,n-sub_size+1):
            # store word in another hashmap
            seen = {}
            for j in range(0, word_count):
                next_word_index = i + j * word_length
                next_word = s[next_word_index:next_word_index+word_length]
                if next_word not in word_freq:
                    break
                if next_word not in seen:
                    seen[next_word] = 0
                seen[next_word] += 1
                if seen[next_word] > word_freq[next_word]:
                    break
                if j+1 == word_count:
                    res.append(i)
        return res

# method 1 alternative approach same idea different implementation
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j: j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer

# method 2 optimized sliding window
# time: O(M+N*b) M=len(words),N=len(s),b = length of each word
# space: O(M+b)
import collections
def findSubstring(s: str, words: list[str]) -> list[int]:
    n = len(s)
    word_count = len(words)
    word_length = len(words[0])
    sub_size = word_count*word_length
    word_map = {}
    for word in words:
        word_map[word] = word_map.get(word, 0) + 1
    res = []

    def sliding_window(left): # O(n/b *2b)
        words_found = collections.defaultdict(int)
        words_used = 0
        excess_word = False
        for right in range(left, n - sub_size + 1, word_length): # n/b total iterations
            next_word = s[right: right+word_length]              # each iteration create a substring O(b)
            if next_word not in word_map: # Mismatched word - reset the window
                words_found = collections.defaultdict(int)
                words_used = 0
                excess_word = False
                left = right + word_length # Retry at the next index
            else: # If we reached max window size or have an excess word
                while right-left == sub_size or excess_word: # perform n/b iterations O(b) time
                    left_word = s[left:left+word_length] # Move the left bound over continously
                    left += word_length
                    words_found[left_word] -= 1
                    if words_found[left_word] == word_map[left_word]: # This word was the excess word
                        excess_word = False
                    else: # Otherwise we actually needed it
                        words_used -= 1
                # Keep track of how many times this word occurs in the window
                words_found[next_word] += 1
                if words_found[next_word] <= word_map[next_word]:
                    words_used += 1
                else:  # Found too many instances already
                    excess_word = True
                if words_used == word_count and not excess_word:
                    res.append(left)

    for i in range(word_length): # b iterations
        sliding_window(i)
    return res

