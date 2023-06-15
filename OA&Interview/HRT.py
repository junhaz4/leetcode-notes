def length_calculator(source):
  res = 0
  string = []
  open_block_commnet = False
  for line in source:
    i = 0
    while i < len(line):
      char = line[i]
      # // comment
      if char == '/' and (i+1) < len(line) and line[i+1] == '/' and not open_block_commnet:
        i = len(line)
      # /* comment
      elif char == '/' and (i+1) < len(line) and line[i+1] == '*' and not open_block_commnet:
        open_block_commnet = True
        i += 1
      # */ comment
      elif char == '*' and (i+1) < len(line) and line[i+1] == '/' and open_block_commnet:
        open_block_commnet = False
        i += 1
      # normal code
      elif not open_block_commnet:
        if char != ' ':
          string.append(char)
      i += 1
    if string and not open_block_commnet:
      res += len(string)
      string = []
  return res 

source = [
  "int a = 2;",
  "int b = 47;/*37;*///41;",
  "int c = 3/*4//5*/;",
  "return a / b * c/*a /* b / c*/;"
]
source = [
  "var a = 2;",
  "/*",
  "var b = 2;",
  "if (a === b) {",
  "  b = a + 1;",
  "  //b = a * 2 + 1;",
  "}",
  "*/",
  "var b = 3;",
  "return a * b;"
]
#print(length_calculator(source))

def add_even(graph):
  odd = 0
  n = len(graph)
  odd_vertices = []
  for i in range(n):
    indegree = 0
    for j in range(len(graph[i])):
      if graph[i][j] == True:
        indegree += 1
    if indegree % 2 == 1:
      odd += 1
      odd_vertices.append(i)
  
  if odd == 0:
    return True
  elif odd == 2:
    v1 = odd_vertices[0]
    v2 = odd_vertices[1]
    for i in range(n):
      if not graph[v1][i] and not graph[v2][i]:
        return True
    return False
  elif odd == 4:
    v1, v2, v3, v4 = odd_vertices[0], odd_vertices[1], odd_vertices[2], odd_vertices[3]
    if ((not graph[v1][v2] and not graph[v3][v4]) or
        (not graph[v1][v3] and not graph[v2][v4]) or 
        (not graph[v1][v4] and not graph[v2][v3])):
      return True
    return False
  else:
    return False

# graph = [[False, True, True, True],
#          [True, False, True, False],
#          [False, True, False, True],
#          [False, False, True, False]]

graph = [[False, True, True, True],
         [True, False, True, False],
         [True, True, False, True],
         [True, False, True, False]]
print(add_even(graph))

# -*- coding: utf-8 -*-
 
def is_solvable(crypt):
  # words = crypt[:2]
  # result = crypt[-1]
  # allWords = crypt
  # firstChars = set(word[0] for word in allWords if len(word) > 1)
  # n = max(map(len, allWords))
  # if len(result) < n: return False
  # def dfs(charIdx, wordIdx, carry, visited, char2digit):
  #     if charIdx == n: return carry == 0
  #     if wordIdx == len(allWords):
  #         # time to check the final status for the current digit
  #         sums = sum(char2digit[word[-charIdx - 1]] if charIdx < len(word) else 0 for word in words) + carry
  #         if sums % 10 == char2digit[result[-charIdx - 1]]:
  #             return dfs(charIdx + 1, 0, sums // 10, visited, char2digit)
  #         else:
  #             return False # prune. To support this, using -charIdx - 1 to visit from right/low to left/high
  #     # current word length is too short to check, move to check next word
  #     if wordIdx < len(words) and charIdx >= len(words[wordIdx]):
  #         return dfs(charIdx, wordIdx + 1, carry, visited, char2digit)

  #     c = allWords[wordIdx][-charIdx-1]
  #     if c in char2digit:
  #         # if current word's curßrent char already map to a digit, continue with next word
  #         return dfs(charIdx, wordIdx + 1, carry, visited, char2digit)
  #     else:
  #         # otherwise try all possibilities via dfs
  #         firstDigit = 1 if c in firstChars else 0
  #         for digit in range(firstDigit, 10):
  #             if digit not in visited:
  #                 visited.add(digit)
  #                 char2digit[c] = digit
  #                 if dfs(charIdx, wordIdx + 1, carry, visited, char2digit.copy()): return True
  #                 visited.remove(digit) # restore visited and char2digit by discarding the copy
  #         return False
  # return dfs(0, 0, 0, set(), {})
  words = crypt[:2]
  result = crypt[-1]
  start = set()
  for word in words + [result]:
      if len(word) > 1:
          start.add(word[0])


  n = max(map(len, words + [result]))
  if len(result) < n:
      return False

  def dfs(idx, i, carry, visited, mp):
      if idx == n:
          return carry == 0
      if i == len(words) + 1:
          sums = sum(mp[word[-idx - 1]] if idx < len(word) else 0 for word in words) + carry
          if sums % 10 == mp[result[-idx - 1]]:
              carry = sums // 10
              return dfs(idx + 1, 0, carry, visited, mp)
          return False

      if (i < len(words) and idx >= len(words[i])):
          return dfs(idx, i + 1, carry, visited, mp)
      tmp = words + [result]
      ch = tmp[i][-idx-1]
      if ch in mp:
          return dfs(idx, i + 1, carry, visited, mp)
      begin = 0
      if ch in start:
          begin = 1
      for x in range(begin, 10):
          if x not in visited:
              visited.add(x)
              mp[ch] = x
              if dfs(idx, i + 1, carry, visited, mp.copy()):
                  return True
              visited.remove(x)
      return False

  return dfs(0, 0, 0, set(), {})

crypt= ["SEND","MORE","MONEY"]
print(is_solvable(crypt))