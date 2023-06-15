def phoneNumberLetterCombinations(letters,digits: str) -> list[str]:
  if len(digits) == 0:
    return []
  letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
  res = []
  path = []
  def backtracking(index):
    if index == len(digits):
      res.append("".join(path[:]))
      return
    ds = letters[digits[index]]
    for digit in ds:
      path.append(digit)
      index += 1
      backtracking(index)
      index -= 1
      path.pop()
  backtracking(0)
  return res

def numberofOrdersInBacklog(orders):
  import heapq
  buy = []
  sell = []
  for price,amount,order_type in orders:
    # buy order
    if order_type == 0: 
      while amount > 0 and sell:
        if sell[0][0] > price:
          break
        deal = min(amount,sell[0][1])
        amount -= deal
        sell[0][1] -= deal
        if sell[0][1] == 0:
          heapq.heappop(sell)
      if amount > 0:
        heapq.heappush(buy,[-price,amount])
    # sell order
    else:
        while amount > 0 and buy:
          if -buy[0][0] < price:
            break
          deal = min(amount,buy[0][1])
          amount -= deal
          buy[0][1] -= deal
          if buy[0][1] == 0:
              heapq.heappop(buy)
        if amount > 0:
          heapq.heappush(sell,[price,amount])
  mod = 10**9+7
  res = (sum([t[1] for t in buy]) + sum([t[1] for t in sell])) % mod
  return res

  
def meeting_schedule(slots1,slots2,duration):
  slots1.sort()
  slots2.sort()
  p1, p2 = 0, 0
  n1, n2 = len(slots1), len(slots2)
  while p1 < n1 and p2 < n2:
    right = min(slots1[p1][1], slots2[p2][1])
    left = max(slots1[p1][0], slots2[p2][0])
    if right - left >= duration:
      return [left,left+duration]
    if slots1[p1][1] > slots2[p2][1]:
      p2 += 1
    else:
      p1 += 1
  return []

def word_search(board: list[list[str]], word: str) -> bool:
  from collections import defaultdict, Counter
  rows, cols = len(board), len(board[0])
  visited = set()
  def backtracking(r,c,i):
    if i == len(word):
        return True
    if (r < 0 or 
        r >= rows or
        c < 0 or 
        c >= cols or
        board[r][c] != word[i] or
        (r,c) in visited):
        return False
    visited.add((r,c))
    res = (backtracking(r+1,c,i+1) or
            backtracking(r-1,c,i+1) or
            backtracking(r,c+1,i+1) or
            backtracking(r,c-1,i+1))
    visited.remove((r,c))
    return res
  # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
  count = defaultdict(int, sum(map(Counter, board), Counter()))
  if count[word[0]] > count[word[-1]]:
    word = word[::-1]
  for r in range(rows):
    for c in range(cols):
        if backtracking(r,c,0):
            return True
  return False 


def random_generator(text,n):
  """
  Generate a random sentence of length N from a given text. Logic:Randomly select a word
  The next word will be the subsequent contagious word from the previously selected word. If the next word occurs multiple times in the sentence, select randomly.
  Continue until length fulfill required length
  Special case: If the chosen word has no next word (last word in the sentence, use first word as the "next word" - assume circular)
  https://leetcode.com/discuss/interview-question/1234140/flexport-amsterdam-coding-interview
  """
  import random
  from collections import defaultdict
  word_hash = defaultdict(list)
  res = []
  seen = set()
  text_split=text.split()
  text_len = len(text_split)
  for j,word in enumerate(text_split):
    word_hash[word].append(j)
  i=random.randrange(0, text_len) ## Initial select for random index
  while n > 0:
    res.append(text_split[i])
    n -= 1
    seen.add(i)
    while (i+1)%text_len in seen:
      i+=1
    next_word_index=(i+1)%text_len
    next_word=text_split[next_word_index]
    rand_word_index=random.randrange(0, len(word_hash[next_word]))
    word_hash[next_word][rand_word_index],word_hash[next_word][-1]=word_hash[next_word][-1],word_hash[next_word][rand_word_index]
    i=word_hash[next_word].pop()
  return "".join(res)

'''
https://www.1point3acres.com/bbs/thread-821179-1-1.html?mobile=2 
Token card games
Given card with cost in terms of tokens. For eg to buy some Card A, you need 3 Blue tokens and 2 Green tokens. Tokens can be of Red, Green, Blue, Black or White color.
Now there is player who is holding some tokens. For eg player has 4 Blue tokens and 2 Green tokens, then player can buy above Card A. Lets say if player only has 2 Blue tokens and 2 Green tokens, then player can not buy Card A above as player is short of 1 Blue token.. check 1point3acres for more.
Write a method that returns true if player can buy the card or false otherwise.
More examples :
Cost of Card : 2 White, 1 Black and 4 Blue
If Player has : 2 White, 2 Black and 4 Blue, method will return true
If Player has : 2 White, 2 Green and 4 Blue, method will return false
Money is represented in number of each color: black, blue, green, green, white. A card has properties of how much it requires by it. Implement a canPurchase() method to decide whether a certain amount of money can buy a card.Implement the purchase method, which should update the money and cards owned. Discount with card owned. Each card has a property of color. If you own cards of a color. Next time purchase of another card, the price of this color can be discounted by the number of card you owned. Update the canPurchase and purchase method.
. ----
1、Implement canPurchase 
2 implement purchase
3、Discount with card owned
(比如手里有三张 Red Card,下一张待购买的卡片 cost 需要 N 个 Red Money,实际购买时 只需要支付 N-3 个 Red Money 就行)
cost: {"Red":4}. .и
player:{"Red":7,"Bule":5}.
purchase()
player:{"Red":3,"Bule":5}
playerCard:{"Red":1}
purchase() ..
player:{"Red":0,"Bule":5}.
playerCard:{"Red":2}
4、Gold color
Money 增加一种 Gold color,万能色，可以在买卡的时候冲抵任何一种颜色。比如 下一张待购买的卡片 cost 需要 N 个 Red Money。手里只有 N-1 个 Red Money, 但是有超 过一个 Gold Money,那也买得起
'''
from collections import defaultdict
from enum import Enum

class Token(Enum):
  R = "RED"
  G = "GREEN"
  B = "BLUE"
  BL = "BLACK"
  W = "WHITE"
  GL = "GOLD"
  
class Card:
  def __init__(self,cost:dict) -> None:
     self.cost = cost
     
  def get_cost(self): # get card cost 
    return self.cost
     
class Player:
  def __init__(self,tokens) -> None:
    self.tokens = tokens
    self.card = {} # store newly bought cards
    
  def get_token(self): # get tokens 
    return self.tokens
  
  def set_card(self,card,value): # update newly bought cards 
    if card in self.card:
      self.card[card] += value
    else:
      self.card[card] = value

class Game:
  def __init__(self,card,player) -> None:
    self.card = card
    self.player = player
  
  def canPurchase(self,card):
    remaining = defaultdict(int)
    for token in card:
      if token not in self.player:
        return False
      else:
        remaining[token] = card[token] - self.player[token]
    for token in remaining:
      if remaining[token] > 0:
        return False
    return True
  
  def purchase(self):
    for card_name in self.cards:
      card = self.cards[card_name]
      if self.canPurchase(card):
        for token in card:
          self.player[token] -= card[token]
        self.player.set_card(card_name,1)
    return self.player_card
  
class TokenCardGames:
  
  def __init__(self,cards,player) -> None:
    self.cards = cards
    self.player = player
    self.player_card = defaultdict(int)
  
  def canPurchase(self,card):
    remaining = defaultdict(int)
    for token in card:
      if token not in self.player:
        return False
      else:
        remaining[token] = card[token] - self.player[token]
    for token in remaining:
      if remaining[token] > 0:
        return False
    return True
  
  def purchase(self):
    for card_name in self.cards:
      card = self.cards[card_name]
      if self.canPurchase(card):
        for token in card:
          self.player[token] -= card[token]
        self.player_card[card_name] += 1
    return self.player_card
  
"""if __name__ == "__main__":
  cards = {}
  cardA = {"WH":2,"BL":1,"B":4}
  cardB = {"WH":2,"BL":1,"B":4}
  cards["cardA"] = cardA
  cards["cardB"] = cardB
  player = {"WH":4,"BL":2,"B":5}
  game = TokenCardGames(cards,player)
  for card_name,card in cards.items():
    print("player can buy " + card_name + ": "+str(game.canPurchase(card)))
  print(game.purchase())
  print(game.player)"""
  
class TokenCardGamesII:
  
  def __init__(self,cards,player):
    self.cards = cards
    self.player = player
    self.player_card = defaultdict(int)
  
  def canPurchase(self,card):
    remaining = defaultdict(int)
    for token in card:
      if token not in self.player:
        return False
      else:
        remaining[token] = card[token]-self.player[token]-self.player_card[token]
    for token in remaining:
      if remaining[token] > 0:
        return False
    return True
  
  def purchase(self):
    for card_name in self.cards:
      card = self.cards[card_name]
      if self.canPurchase(card):
        for token in card:
          self.player[token] = self.player[token] - card[token] + self.player_card[token]
        self.player_card[card_name] += 1
    return self.player_card
  
"""if __name__ == "__main__":
  cards = {}
  red_card = {"R":4}
  cards["R"] = red_card
  player = {"R":7,"B":2,"BL":5}
  gameII = TokenCardGamesII(cards,player)
  for card_name, card in cards.items():
    print("player can buy " + card_name + ": "+str(gameII.canPurchase(card)))
  print(gameII.purchase())
  print(gameII.player)
  print()
  print(gameII.purchase())
  print(gameII.player)"""
  
class TokenCardGamesIII:
  def __init__(self,cards,player):
    self.cards = cards
    self.player = player
    self.player_card = defaultdict(int)
    
  def canPurchase(self,card):
    remaining = defaultdict(int)
    for token in card:
      if token not in self.player:
        return False
      else:
        remaining[token] = card[token] - self.player[token] - self.player_card[token]
    for token in remaining:
      if remaining[token] > 0:
        if "Gold" in self.player:
          temp = self.player["Gold"]
          while self.player["Gold"] > 0:
            remaining[token] -= 1
            self.player["Gold"] -= 1
            if remaining[token] <= 0:
              break
          if remaining[token] > 0:
            return False
        self.player["Gold"] = temp
    return True
  
  def purchase(self):
    for card_name in self.cards:
      card = self.cards[card_name]
      if self.canPurchase(card):
        for token in card:
          remain = self.player[token] - card[token] + self.player_card[token]
          if remain > 0:
            self.player[token] = remain
          else:
            if self.player['Gold'] > -remain:
              self.player[token] = 0
              self.player["Gold"] = self.player["Gold"] + remain
        self.player_card[card_name] += 11
    return self.player_card

"""if __name__ == "__main__":
  cards = {}
  red_card = {"R":4}
  cards["R"] = red_card
  player = {"R":6,"B":2,"BL":5,"Gold":5}
  gameIII = TokenCardGamesIII(cards,player)
  for card_name, card in cards.items():
    print("player can buy " + card_name + ": "+str(gameIII.canPurchase(card)))
  print(gameIII.purchase())
  print(gameIII.player)
  print()
  print(gameIII.purchase())
  print(gameIII.player)"""

'''
Board Gamec, board and array of piece
题目是有一个checker棋盘 顶上都是黑棋，最底下都是白棋， 两个玩家轮流走棋 每一步黑棋只能走左下和右下 白棋只能走左上和右上。问如果给一个现在棋盘的state  state就是棋盘上现在所有棋的位置和轮到哪个玩家  返回all possible moves。input, output和棋盘的state自己随便选data structure。。为了方便楼主棋盘就用了个2D char array  然后定义了一个Coordinate类用来记录棋子的位置 然后用一个List在存一个start和end coordinate来表示一个possible move 最后返回一个List<List<Coordinate>> 先说了个brute force solution给他 就遍历整个棋盘。。然后我说这个应该不是很好的解法，但他直接说他不是很在意最优解 写出来比较重要。15分钟写完了之后小哥说好 follow-up来优化一下 因为可以不需要检查是白棋还是黑棋 楼主就define了个offset = +1/-1 来表示往上走还是往下走 搜索周围的时候就直接i+offset
一个棋盘,两个对手,没有block
上面对手只能往下走，往斜对角走
下面对手只能往上走 往斜对角走
1. getAllNextMove(turn,board)
获取黑棋和白棋当前状态所有可以走的步骤
input: true白棋在右下角 false黑旗在左上角
output: list包含所有可能走的步骤
要validate board的null length 每个row的length player是不是X O  或者empty
2. canMove(current,target,turn)
判断当前位置能否到达指定位置
3. move(current,target,turn)
移动到当前位置
面试官说可以假设board已经存在class里了 PS 我真不知道怎么存 他说随意 我就constructor传进来的 
需要validate这个move是不是valid 因为move可以长度超过1 可以src不可以是empty的 dst必须要empty 而且X/O的需要向上和向下的那两个
面试官最后还问了，什么能改动
player 其实可以是个enum board也是enum[][]
eg
1  1 0 0 0 
2  0 1 0 0 
3  0 0 2 0 
4  0 0 0 2
getallnextmove(false)
output: [[2,0]]
canmove([1,1],[3,1],true)
output: true
move([1,1],[3,1],true)
ouput:none
updated board:
1  1 0 0 0 
2  0 1 0 0 
3  1 0 2 0 
4  0 1 0 2
'''
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
  
'''
flight checking system
flight with departure, arrivial, price, flight name
1. if there is direct flight from a to b
2. if there is indirect flight from a to b
3. if there is a shortest path from a to b
4. if there is a cheapest path from a to b
'''
from collections import defaultdict,deque
class Flight:
  
  def __init__(self) -> None:
    self.flight_map = defaultdict(dict) # {"A":{"B":["price","name"]...}...}
    self.cities = [] # contains all cities
    
  def direct_arrive(self,cityA,cityB):
    return cityB in self.flight_map[cityA]
  
  def indirect_arrive(self,cityA,cityB):
    flight_que = deque()
    flight_que.append(cityA)
    visited = set()
    visited.add(cityA)
    while flight_que:
      stop = flight_que.popleft()
      if stop == cityB:
        return True
      for city in self.flight_map[stop]:
        if city not in visited:
          visited.add(city)
          flight_que.append(city)
    return False
  
  def shortest_path(self,cityA,cityB): # number of stops BFS
    if self.direct_arrive(cityA,cityB):
      return True
    else:
      flight_map = {cityA:None} # dest: src
      distance = {cityA:0}
      flight_que = deque()
      flight_que.append((cityA,0))
      visited = set()
      visited.add(cityA)
      while flight_que:
        flight,stop = flight_que.popleft()
        if flight in visited:
          continue
        if flight == cityB:
          return stop
        for city in self.flight_map[flight]:
          if city not in visited: 
            visited.add(city)
            flight_que.append(city)
            distance[city] = distance[flight] + 1
            flight_map[city] = flight
    
  def cheapest_path(self,cityA,cityB): # cheapest flight 
    import heapq
    dist = {v:float('inf') for v in self.cities}
    dist[cityA] = 0
    visited = set()
    flight_que = [[0,cityA]]
    while flight_que:
      cost, city = heapq.heappop(flight_que)
      if city in visited:
        continue
      visited.add(city)
      for nei, info in self.flight_map[city].items():
        if nei in visited:
          continue
        new_cost = info[0] + cost
        if new_cost < dist[nei]:
          dist[nei] = new_cost
          heapq.heappush(flight_que,[new_cost,nei])
    return dist[cityB]
  

'''
https://leetcode.com/discuss/interview-question/1777636/
https://leetcode.com/discuss/interview-question/1777636/Flexport-or-Phone-Screen-or-Calculate-Time-To-Travel-Through-The-City
Below is a section of a city with roads and stop lights. The letters indicate entry points where we measure traffic flow.
Each intersection has a traffic light - We want to build a program to simulate traffic flowing through the city so we can
test traffic light control algorithms with sample data.
For purposes of this exercise, your simulation should operate on 1 minute intervals,
where every minute lights (potentially) change and cars drive along roads, with each section of road taking 1 minute to drive.
eg:
       J    
       |    
  A ---🚦---
       |     
  B ---🚦---
       | 
       
Example of traffic flow::
A car enters road J at minute 2
It takes 1 minute to drive to light A-J
Once light A-J is green for road J, it takes 1 minute to drive to light B-J
Once light B-J is green for road J, it takes 1 minute to drive to the exit of the city
Total travel time would be 3 minutes + number of minutes spent waiting at lights
Assuming the car hit only green lights, it would exit the city at minute 5

PART 1
Let's start by simulating one road - Road J.
First, create a data model to represent the road, lights, and cars driving along it.
Next, enter one car into the road and write a function that simulates time in 1 minute intervals,
moving the car along the road and stopping it at red lights until they turn green. It should run until the car has exited the city.
For right now we can use a simple traffic light control: Start with both lights green on the first minute,
and then toggle back and forth between red and green each minute after that.
Your function should return the total time it took the car to travel through the city.
1. 一条路, 一个车
2. 多条路, 一个车
3. 多条路, 多个车
'''
class Light:
  def __init__(self,x,y,is_green=True):
    self.x = x
    self.y = y
    self.is_green = is_green
    
class Road:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  @property
  def is_vertical(self):
    return self.y == None

class Car:
  def __init__(self,x,y,direction): # 0 => increasing y, 1 => increasing x, 2 => decreasing y, 3 => decreasing x
    self.x = x
    self.y = y
    self.direction = direction

class Map:
  def __init__(self,roads,limits_min,limits_max):
    self.lights = []
    for r1 in roads:
      for r2 in roads:
        if r1.is_vertical and not r2.is_vertical:
          self.lights.append(Light(r1.x,r2.y))
    self.roads = roads
    self.city_limits_min = limits_min
    self.city_limits_max = limits_max
  
  def simulation(self,car):
    total_time = 0
    while self.city_limits_min[0] <= car.x <= self.city_limits_max[0] and self.city_limits_min[1] <= car.y < self.city_limits_max[1]:
      total_time += 1
      if not any((light.x, light.y) == (car.x, car.y) and not light.is_green for light in self.lights):
        if car.direction == 0: car.y += 1
        if car.direction == 1: car.x += 1
        if car.direction == 2: car.y -= 1
        if car.direction == 3: car.x -= 1
      for light in self.lights:
        light.is_green = not light.is_green
    return total_time

J = Road(1, None)
A = Road(None, 1)
B = Road(None, 2)

m = Map([J, A, B], (0, 0), (2, 3))
#assert m.simulation(Car(1, 0, 0)) == 5
