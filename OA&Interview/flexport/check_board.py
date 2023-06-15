def initialize_board():   
  coordinates_1 = set()
  coordinates_2 = set()  
  board = [[0]*8 for _ in range(8)]    
  for i in range(4):             
    if i % 2 == 0:                 
      for j in range(0, 8, 2):                     
        board[i][j] = "1"                     
        coordinates_1.add((i, j))            
    else:                 
      for j in range(1, 8, 2):                     
        board[i][j] = "1"                
        coordinates_1.add((i, j))         
  for i in range(7, 3, -1):             
    if i % 2 == 1:                 
      for j in range(0, 8, 2):                     
        board[i][j] = "2"                     
        coordinates_2.add((i, j))             
    else:                 
      for j in range(1, 8, 2):                     
        board[i][j] = "2"                     
        coordinates_2.add((i, j))
  return board

#true白棋=2在右下角 false黑旗=1在左上角
import copy
class Game:
  def __init__(self,board,n) -> None:
    self.board = board
    self.length = n
    self.temp_board = copy.deepcopy(self.board)
    
  def canMove(self,current,target,is_white):
    x = current[0]
    y = current[1]
    targetx = target[0]
    targety = target[1]
    return self.moveNextStep(self.temp_board, x, y, targetx, targety, is_white)
  
  def moveNextStep(self,board, x, y, targetx, targety, is_white):
    if x == targetx and y == targety:
      return True
    if (not self.in_area(x,y)) or (is_white and targetx > x) or ( not is_white and targetx < x):
      return False
    res = False
    temp = board[x][y]
    if is_white:
      if board[x][y] != "1":
        board[x][y] = "2"
        res = self.moveNextStep(board,x-1,y-1,targetx,targety,is_white) or self.moveNextStep(board,x-1,y+1,targetx,targety,is_white)
        if not res:
          board[x][y] = temp
    else:
      if board[x][y] != "2":
        board[x][y] = "1"
        res = self.moveNextStep(board,x+1,y-1,targetx,targety,is_white) or self.moveNextStep(board,x+1,y+1,targetx,targety,is_white)
        if not res:
          board[x][y] = temp
    return res 
  
  def move(self,current,target,is_white):
    if self.canMove(current,target,is_white):
      if is_white:
        self.temp_board[target[0]][target[1]] = "2"
      else:
        self.temp_board[target[0]][target[1]] = "1"
      self.board = copy.deepcopy(self.temp_board)
    else:
      print("Target position cannot be reached, please retry")
  
  def in_area(self,i,j):
    return 0 <= i < self.length and 0 <= j < self.length
  
  def getNextStep(self,i,j,steps,is_white):
    if not self.in_area(i,j):
      return 
    if self.board[i][j] == "0":
      steps.append([i,j])
      return 
    if is_white:
      if self.board[i][j] == "2":
        self.getNextStep(i-1,j-1,steps,is_white)
        self.getNextStep(i-1,j+1,steps,is_white)
    else:
      if self.board[i][j] == "1":
        self.getNextStep(i+1,j-1,steps,is_white)
        self.getNextStep(i+1,j+1,steps,is_white)
    
  def getAllNextStep(self,is_white): # true白棋在右下角 false黑旗在左上角
    steps = []
    if is_white:
      self.getNextStep(self.length-1,self.length-1,steps,is_white)
      # for i in range(self.length):
      #   for j in range(self.length):
      #     if self.board[i][j] == "2":
      #       self.getNextStep(i,j,steps,is_white)
    else:
      self.getNextStep(0,0,steps,is_white)
      # for i in range(self.length):
      #   for j in range(self.length):
      #     if self.board[i][j] == "1":
      #       self.getNextStep(i,j,steps,is_white)
    return steps
  
"""if __name__ =="__main__":
  n = 4
  board = [["1","0","0","0"],
           ["0","1","0","0"],
           ["0","0","2","0"],
           ["0","0","0","2"]]
  # n = 8
  # board = initialize_board()
  game = Game(board,n)
  black = game.getAllNextStep(False)
  print(black)
  current = [1,1]
  target = [3,1]
  res = game.canMove(current,target,False)
  print(res)
  game.move(current,target,False)
  print(game.board)"""
  