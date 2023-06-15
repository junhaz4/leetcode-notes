import collections
def anagrams(lst):
    hash_map = collections.defaultdict(list)
    for string in lst:
        key = ''.join(sorted(string))
        hash_map[key].append(string)
    res = []
    for key, value in hash_map.items():
        if len(value) >= 2:
            res.append(value)
    return res

# time complexity: O(n*k*logk) k=length of word, n = length of lst
