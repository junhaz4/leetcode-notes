# lc 150 polish calculator
import math
def evalRPN(tokens):
  stack = []
  for token in tokens:
      if token in "+-*/":
          number_2 = stack.pop()
          number_1 = stack.pop()
          result = 0
          if token == "+":
              result = number_1 + number_2
          elif token == "-":
              result = number_1 - number_2
          elif token == "*":
              result = number_1 * number_2
          else:
              result = int(number_1 / number_2)
          stack.append(result)
      elif token == "sqrt":
          number = stack.pop()
          number = math.sqrt(number)
          stack.append(number)
      else:
          stack.append(int(token))
  return stack.pop()


# two sum, find paris in an array that sums to a target
def two_sum(nums,target):
  hashmap = {}  # num[i]:i
  for i, n in enumerate(nums):
      complement = target - n
      if complement in hashmap:
          return [i,hashmap[complement]]
      hashmap[n] = i
  return [-1,-1]

def getPairsCount(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count

# lc888  A and B has different number of candidies and A and B choose to swap candies such that they have the same amount of candies, return the number of candies they each choose to swap
def fair_candy_swap(aliceSizes, bobSizes):
  '''
  a_total = sum(aliceSizes)
  b_total = sum(bobSizes)
  if a_total == b_total:
      return [0,0]
  setb = set(bobSizes)
  for a in aliceSizes:
      expected = (b_total-a_total)/2 + a
      if expected in setb:
          return [a,int(expected)]
  '''
  a_total = sum(aliceSizes)
  b_total = sum(bobSizes)
  if a_total == b_total:
      return [0,0]
  half = (a_total+b_total)/2
  diff = a_total - half
  setb = set(bobSizes)
  for a in aliceSizes:
      if a-diff in setb:
          return [a,a-diff]
        
# lc384 shuffel an array
import random
class Solution:
    def __init__(self, nums):
      self.nums = list(nums) # used for reset, no manipulation on this variable
      self.array = nums

    def reset(self):
      self.array = self.nums
      self.nums = list(self.nums)
      return self.array

    def shuffle(self):
      for i in range(len(self.array)):
          swap_idx = random.randrange(i,len(self.array))
          self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
      return self.array
    
# implementation of circular linked list
class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

class CircularlinkedList:
  def __init__(self):
    self.last = None 
  
  def is_empty(self):
    return self.last == None
  
  def addToEmpty(self, val):
    if self.last != None:
        return self.last
    newNode = Node(val)
    self.last = newNode
    self.last.next = self.last
    return self.last
  
  def add_front(self,val):
    if self.is_empty():
      return self.addToEmpty(val)
    else:
      new_node = Node(val)
      new_node.next = self.last.next
      self.last.next = new_node
    return self.last
  
  def add_end(self,val):
    if self.is_empty():
      return self.addToEmpty(val)
    new_node = Node(val)
    new_node.next = self.last.next
    self.last.next = new_node
    self.last = new_node
    return self.last
  
  def add_after(self,val,node):
    if self.last == None:
      return None
    new_node = Node(val)
    cur = self.last.next
    while cur:
      if cur == node:
        new_node.next = cur.next 
        cur.next = new_node
        if cur == self.last:
          self.last = new_node
          return self.last
        else:
          return self.last
      cur = cur.next
      if cur == self.last.next:
        print('given node not in linkedlist')
        break
  def delete_node(self,node):
    if self.last == None:
      return None
    # when there is only one node
    if self.last == node and self.last.next == self.last:
      self.last = None
    
    cur = self.last 
    temp = None
    # if last node is to be deleted
    if self.last == node:
      # find the node before the last node
      while cur.next != self.last:
        cur = cur.next
      cur.next = self.last.next
      self.last = cur.next 
    # if deleted node is in middle
    while cur.next != self.last and cur.next != node:
      cur = cur.next 
    # if node to be deleted was found
    if cur.next == node:
      temp = cur.next
      cur.next = temp.next 
    return self.last 
  
  def traverse(self):
    if self.last != None:
      cur = self.last.next
      while cur:
        print(cur)
        cur = cur.next 
        if cur == self.last.next:
          break

def calculate(s: str) -> int:
  def calc(it):
    def update(op, v):
      if op == "+": stack.append(v)
      if op == "-": stack.append(-v)
      if op == "*": stack.append(stack.pop() * v)
      if op == "/": stack.append(int(stack.pop() / v))
    num, stack, sign = 0, [], "+"
    while it < len(s):
        if s[it].isdigit():
            num = num * 10 + int(s[it])
        elif s[it] in "+-*/":
            update(sign, num)
            num, sign = 0, s[it]
        elif s[it] == "(":
            num, j = calc(it + 1)
            it = j - 1
        elif s[it] == ")":
            update(sign, num)
            return sum(stack), it + 1
        it += 1
    update(sign, num)
    return sum(stack)
  return calc(0)


# inline vs block vs inline-block https://stackoverflow.com/questions/9189810/css-display-inline-vs-inline-block

def add(a,b):
  """Calculate sum of two numbers

  Args:
      a (int): A decimal integer
      b (int): A decimal integer

  Returns:
      int: sum of a and b
  """
  return a+b
#print(add.__doc__)

class Person:
  """A class to represent a person.
  
  Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    get():
        Prints the person's name and age.
  """
  def __init__(self,name,surname,age):
    """Constructs all the necessary attributes for the person object.

    Args:
        name (str): _description_
        surname (str): _description_
        age (int): _description_
    """
    self.name = name
    self.surname = surname
    self.age = age
  def get(self):
    """Prints the person's name and age.
    """
    print(f'My name is {self.name} {self.surname}. I am {self.age} years old.')
#print(Person.__doc__)
    


value = 1
print("Record with value %s" % value)