from collections import defaultdict
def check_solution(board):
  rows = defaultdict(set)
  cols = defaultdict(set)
  square = defaultdict(set) # key: pair(row/3, col/3)
  for row in range(9):
    for col in range(9):
      if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in square[(row//3,col//3)]:
        return False 
      rows[row].add(board[row][col])
      cols[col].add(board[row][col])
      square[(row//3,col//3)].add(board[row][col])
      
  return True
# TIME COMPLEXITY: O(N^2) where n is 9

def check_solution_2(board):
  # using array
  rows = [[0]*9 for _ in range(9)]
  cols = [[0]*9 for _ in range(9)]
  squares = [[0]*9 for _ in range(9)]
  for row in range(9):
    for col in range(9):
      # check the each row 
      position = board[row][col]-1
      if rows[row][position] == 1:
        return False
      # check each column
      rows[row][position] = 1
      if cols[col][position] == 1:
        return False 
      cols[col][position] = 1
      # check each square 
      idx = (row//3)*3+col//3
      if squares[idx][position] == 1:
        return False
      squares[idx][position] = 1
  return True

def get_sum_recursive(string):
  n = len(string)
  vowels = {"a":1, "e":2, "i":3, "o":4, "u":5}
  res = 0
  def helper(index):
    nonlocal res
    if index == n:
      return 
    if string[index] in vowels.keys():
      res += vowels[string[index]]
    helper(index+1)
  helper(0)
  return res


from collections import defaultdict
def get_sum_vowels(string):
  res = 0
  vowels = {"a":1, "e":2, "i":3, "o":4, "u":5}
  count = defaultdict(int)
  for char in string:
    if char in vowels:
      count[char] += 1
  for char in count.keys():
    res += vowels[char]*count[char]
  return res


import re
exp = re.compile('AB|AG|AS|Ltd|KB|University')
search_str = "Hello test AB"
if re.search(exp, search_str):
  print ("Contains the word")
else:
  print ("Does not contain the word")
  