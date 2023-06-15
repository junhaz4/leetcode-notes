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
  
  
B = {"B":4,"W":3}  
player = {"B":7,"W":5} 
