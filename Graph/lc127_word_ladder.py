import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Method 1 Hashmap + BFS
        '''
        Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
                         hit
                   /      |      \
                   *it   h*t   hi*
                 /|\     /|\     /|\
        # In order to continue the  Breath First Search(BFS) process,
        # we need to know the children of *it, h*t, and hi*.
        # so we need the information from word list.

        wordList = ["hot","dot","dog","lot","log","cog"]
        change_map ={ *ot : hot, dot, lot
                      h*t : hot
			          ho* :hot
			          d*t : dot
			          do* : dot, dog
			          *og : dog, log, cog
			          d*g : dog
                      l*t : lot
                      lo* : lot, log
                      l*g : log
                      c*g: cog
                      co* : cog}


                                        hit, level = 1
						   /                 |                   \
					     *it                h*t                  hi*
						   |                 |                     |
			             null  	       hot ,level = 2            null
								/            |       \
								/            |        \
				               *ot           h*t      ho*
				           /    |   \         |        |
                     hot,2   dot,3  lot,3   hot,2    hot,2


        # as we can see,  "hot" has been visited in level 2, but "hot" will still appear at the next level.
        # To avoid duplicate calculation, we keep a visited map,
        # if the word in the visited map, we skip the word, i.e. don't append the word into the queue.
        # if the word not in the visited map, we put the word into the map, and append the word into the queue.
        '''
        # check if the endWord is in wordList
        if endWord not in wordList:
            return 0
        # create the hashmap-dict
        nei = collections.defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i + 1:]
                nei[pattern].append(word)

        visited = {beginWord}
        q = collections.deque([beginWord])
        step = 1
        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                if word == endWord:
                    return step
                for j in range(L):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neiw in nei[pattern]:
                        if neiw not in visited:
                            visited.add(neiw)
                            q.append(neiw)
            step += 1
        return 0

# Method 2 Hashset + BFS
def ladderLength(beginWord, endWord, wordList):
    wordList = set(wordList)
    queue = collections.deque([[beginWord, 1]])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    # remove the word founded to avoid duplicate calculation
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])
    return 0

# Method 3 Bidirectional BFS - start + end
def ladderlength( beginWord, endWord, wordList):
    wordDict = set(wordList)
    if endWord not in wordDict:
        return 0
    L = len(beginWord)
    q1 = {beginWord}
    q2 = {endWord}
    wordDict.remove(endWord)
    step = 0
    while len(q1)>0 and len(q2)>0:
        step += 1
        if len(q1) > len(q2):
            q1,q2 = q2,q1
        q = set()
        for w in q1:
            new_words = [
                w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in range(L)]
            for new_word in new_words:
                if new_word in q2:
                    return step + 1
                if new_word not in wordDict:
                    continue
                wordDict.remove(new_word)
                q.add(new_word)
        q1 = q
    return 0



