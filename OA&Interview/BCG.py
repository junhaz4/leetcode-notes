"""Given two strings, determine if they share a common substring. A substring may be as small as one character. 
s1 = 'the' s2 = 'bed' These share the common substring 'e'. 
s1 = 'xyz' s2 = 'abc' These do not share a substring. 
Function Description Write a function with the following parameter(s): string s1: a string string s2: another string Returns string: either YES or NO"""
def checkCommonSubstring(s1,s2):
  '''
  # brute force, compare each string in s1 with string in s2
  # time complexity: O(n^2), space O(1)
  for c1 in s1:
    if c1 in s2:
      return True 
  return False  
  '''
  # time complexity: O(n), space O(n)
  char_map = [0]*26
  for c1 in s1:
    char_map[ord(c1)-ord('a')] = 1
  for c2 in s2:
    if char_map[ord(c2)-ord('a')] == 1:
      return "YES"
  return "NO"

def findCommonSubstring(s1,s2):
  m, n = len(s1), len(s2)
  # dp[i][j]: 以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]
  dp = [[0]*(n+1) for _ in range(m+1)]
  res = 0
  start, end = 0, 0
  for i in range(1,m+1):
    for j in range(1,n+1):
      if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
        if res < dp[i][j]:
          res = dp[i][j]
          start, end = i, j
      #res = max(res,dp[i][j])
  s = [0]*res
  length = res
  # traverse diaonally from (start,end) until reach 0
  while dp[start][end] != 0:
    length -= 1
    s[length] = s1[start-1]
    start -= 1
    end -= 1
  return res, "".join(s)
'''
  dp = [0] * (len(B) + 1)
    result = 0
    for i in range(1, len(A)+1):
        for j in range(len(B), 0, -1):
            if A[i-1] == B[j-1]:
                dp[j] = dp[j-1] + 1
            else:
                dp[j] = 0 #注意这里不相等的时候要有赋0的操作
            result = max(result, dp[j])
    return result
'''

"""
you are given a list of projects and dependencies. topological sort & bfs 
graph = {"a": ["b", "c", "d"],  "b": ["e"], # -> []  "c": ["e"], # -> []  "d": [],   "e": [] }
# one valid answer: d -> e -> b -> c -> a  
"""
class Solution:
  def buildOrder(self,graph):
    topo_order = []
    visited = set()
    que = []
    '''
    indegree = [0]*26
    for key in graph.keys():
      for v in graph[key]:
        indegree[ord(v)-ord('a')] += 1
    '''
    for key in graph.keys():
      if len(graph[key]) == 0:
        que.append(key)
    while que:
      project = que.pop(0)
      if project in visited:
        continue
      topo_order.append(project)
      visited.add(project)
      self.remove(topo_order,graph)
      for key in graph:
        if len(graph[key]) == 0 and key not in visited:
          que.append(key)
    return ''.join(topo_order) if len(visited) == len(graph) else None
  def remove(self,order,graph):
    for project in order:
      for dependency in graph.values():
        if project in dependency:
          idx = dependency.index(project)
          del dependency[idx]

'''
lc 249 group shifted strings
Caesar Cipher Encrpytion
You are given a list of string, group them if they are same after using Ceaser Cipher Encrpytion.
Definition of "same", "abc" can right shift 1, get "bcd", here you can shift as many time as you want, the string will be considered as same.
'''
import collections
def groupStrings(strings):
  groups = collections.defaultdict(list)
  for s in strings:
      pattern = ()
      for i in range(1,len(s)):
          pattern = pattern + ((ord(s[i]) - ord(s[i-1]) + 26 ) % 26,)
      groups[pattern].append(s)
  return groups.values()

# From A to z: 65-122
# input list contains characters in lowercase and uppercase and some special characters
def caesar_cipher(string,k): # k is number of shifts
  # len(symbols_up) = len(symbols_low) = 26, add %26 to apply rotation without exceeding the allowed integer value
  n = len(string)
  res = ''
  for i in range(n):
    if string[i].isalpha():
      if string[i].isupper():
        res+=chr(ord('A')+(ord(string[i])-ord('A')+k)%26)
      else:
        res+=chr(ord('a')+(ord(string[i])-ord('a')+k)%26) 
    else:
      res += string[i]
  return res
'''
def solution(string,addNum)
  string = list(string)
  length = len(string)
  for i in range(length):
    if ord(string[i]) <= ord("Z") and ord(string[i]) >= ord("A"):
      asciiCode = ord(string[i]) + addNum
      while asciiCode > ord("Z"):
        asciiCode = asciiCode - ord("Z") + ord("A") - 1
      string[i] = chr(asciiCode)
    elif ord(string[i]) <= ord("z") and ord(string[i]) >= ord("a"):
      asciiCode = ord(string[i]) + addNum
      while asciiCode > ord("z"):
        asciiCode = asciiCode - ord("z") + ord("a") - 1
      string[i] = chr(asciiCode)
return "".join(string)
'''

# wiggle sort
def wiggle_sort(nums):
  # method 1
  # i is odd, nums[i] >= nums[i-1]
  # i is even, nums[i] <= nums[i-1]
  for i in range(1,len(nums)):
    if (i%2 == 0 and nums[i] > nums[i-1]) or (i%2 == 1 and nums[i]< nums[i-1]):
      nums[i-1], nums[i] = nums[i], nums[i-1]
  # method 2
  prev = True
  for i in range(len(nums)-1):
    if prev:
      if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    else:
      if nums[i] < nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    prev = not prev
    
    
# insert into BST
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def insertIntoBST(self, root, val: int):
    """ 
    # recursion
    if not root:
        return TreeNode(val)
    if root.val < val:
        root.right = self.insertIntoBST(root.right,val)
    else:
        root.left = self.insertIntoBST(root.left,val)
    return root
    """
    # iteration
    if not root:
        return TreeNode(val)
    cur = root
    while cur:
      if val > cur.val:
        if cur.right == None:
          cur.right = TreeNode(val)
          return root
        else:
          cur = cur.right
      else:
        if cur.left == None:
          cur.left = TreeNode(val)
          return root
        else:
          cur = cur.left
# delete into BST
class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None
        if root.val < key :
            root.right = self.deleteNode(root.right, key)
        elif root.val > key :
            root.left = self.deleteNode(root.left, key)
        # 找到了要删除的节点，根据以下情况处理
        else:
            # 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
            if not root.left and not root.right:
                return None
            # 第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
            elif root.left and not root.right:
                return root.left
            #第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
            elif not root.left and root.right:
                return root.right
            #第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置并返回删除节点右孩子为新的根节点。
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                temp.left = root.left
                root = root.right
        return root
          
class Solution:
  def sumEvenGrandparent(self, root: TreeNode) -> int:
    """
    # recursion
    res = 0
    def traverse(node,parent,grandparent):
        nonlocal res 
        if not node:
            return 
        if node and grandparent and grandparent.val % 2 == 0:
            res += node.val
        traverse(node.left,node,parent)
        traverse(node.right,node,parent)
    traverse(root,None,None)
    return res 
    """
    # iteration 
    cur_par_grand = [[root,None,None]]
    res = 0
    while cur_par_grand:
        cur, parent, grandparent = cur_par_grand.pop()
        if cur and parent and grandparent and grandparent.val%2 == 0:
            res += cur.val
        if cur.left:
            cur_par_grand.append([cur.left,cur,parent])
        if cur.right:
            cur_par_grand.append([cur.right,cur,parent])
    return res 
  
### OOP
'''
A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods. 
A object is an entity that has a state and behavior associated with it
self represent the instance of the class and is always pointering the current object. By using the “self” we can access the attributes and methods of the class in python. It binds the attributes with the given arguments
The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

Inheritence: single/multilevel/Hierarchical/Hybrid
Inheritance is a way of creating a new class using attributes and methods of an existing class without modifying it. 
Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.
Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class
Multiple level inheritance enables one derived class to inherit properties from more than one base class
use the super() function inside the __init__(),this allows to run the __init__() of the parent class inside the child class.
super() lets you avoid referring to the base class explicitly

Polymorphism
Polymorphism is an ability to use a common interface for multiple forms.
eg two classes of animials, both has run function. Then a common interface function that takes object as parameter and call the object's run function. Then we can pass those tow objects and run it

Encapsulation
It puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data
private variable: use double underscore before it and cannot access it => __classname__variablename
protected vairable: use single underscore, but can access it, it indicates to other programmers that the attribute or method is intended to be be used inside that class. However, privacy is not enforced in any way.

Abstraction
is the process of handling complexity by hiding unnecessary information from the user, 
abstraction can be achieved by having/using abstract classes and methods in our programs.
An abstract method in a base class identifies the functionality that should be implemented by all its subclasses.
A class containing abstract methods is called abstract class. Python provides the abc module to use the abstraction
When we use the TV remote to increase the volume. We don't know how pressing a key increases the volume of the TV. We only know to press the "+" button to increase the volume. That is exactly the abstraction that works in the object-oriented concept

Methods vs Constructors
Methods
Method name can be any name.
With respect to one object one method can be called for n members of lines
Methods are used to represent business logic to perform the operations

Constructor
Constructor will be executed automatically whenever we create a object.
With respect to one object one constructor can be executed only once
Constructors are used to define & initialize the non static variable
'''
### magic function
'''
Magic methods in Python are the special methods that start and end with the double underscores. They are also called dunder methods. Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.
Magic methods are most frequently used to define overloaded behaviours of predefined operators in Python, operator overlaoding
Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because + operator is overloaded by int class and str class.
'''
### decorator & generator & iterator
'''
A decorator is a function that adds functionality to another function without modifying it/wrap a function, modifying its behavior.

A generator is a function that returns an object (iterator) which we can iterate over (one value at a timeare iterators, 
Generators do not store all the values in memory, they generate the values on the fly.
Generator function uses yield not return. yield returns a value and pauses the execution while maintaining the internal states and later continue from there, whereas the return statement returns a value and terminates the execution of the function.
generator expressions are surrounded by parenthesis ()
Generator objects are used either by calling the next method on the generator object or print using the generator object in a for loop

A interator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method. It uses the next() method for iteration.
'''
### instancemethod & staticmethod vs classmethod
'''
instance method: regular method in class, taking self as parameter that points to an instance when called, can freely access attributes and other methods on the same object. Cannot call instance method without creaing a instance first 

class method: has a @classmethod decorator, taking cls as parameter that points to the class—and not the object instance—when called. Because the class method only has access to this cls argument, it can't modify object instance state.

staticmethod: @staticmethod decorator, can neither access and modify object state nor class state. They behave like plain functions except that you can call them from an instance or the class. Staticmethods are used to group functions which have some logical connection with a class to the class.
class MyClass:
    def method(self):
        return 'instance method called', self
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'
'''
### multithreading 
'''
A process is an instance of a computer program that is being executed
A thread is an entity within a process that can be scheduled for execution.
Multithreading is running several different programs at the same time concurrently by invoking multiple threads/ allows us to execute multiple threads at once
The GIL (Global Interpreter Lock) ensures that a single thread executes at a time. A thread holds the GIL and does a little work before passing it on to the next thread. This makes for an illusion of parallel execution. But in reality, it is just threaded taking turns at the CPU
The Global Interpreter Lock (GIL). CPython (the most common Python implementation) is not fully thread safe. In order to support multi-threaded Python programs, CPython provides a global lock that must be held by the current thread before it can safely access Python objects. As a result, no matter how many threads or processors are present, only one thread is ever being executed at any given time
SchedulingL: amount multiple threads, it decides which thread runs the first, hong long it should run and who is the next 
Multiprocessing allows you to run multiple unrelated processes simultaneously. These processes do not share their resources and communicate through IPC
'''
### duck typing
'''
Duck typing is used in dynamic language. 
With Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.
Duck-typing emphasis what the object can really do, rather than what the object is.比如list.extend(), we don't care if the parameter is a list, as long as it can be iterable, such as list/tuple/dict/string
'''
### Python dictionary
'''
dictionary is based on hashmap. A hash value/hash code of the key is computed using a hash function, The hash value addresses a location in an array of “buckets” or “collision lists” which contains the (key , value) pair. Python uses Open Addressing to resolve hash collision
'''
### Garbage collection & memory management
'''
Garbage collection is a predefined program removing unused or unreferenced objects from the memory location, it uses references counting  
Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter.
When exit python, not all memory de-allocated such as memory reserved by the C library and modules with circular references to other objects, or to objects referenced from global namespaces, aren't always freed on exiting Python
'''
### immutable vs mutable variables
'''
The objects which doesn't allow to modify the contents: string/tuple/number/bool
The Objects which allows to modify the contents: list/set/dict
Immutable objects performance is high. Applying iterations on Immutable objects takes less time.
'''
### python function arguments
'''
Python uses pass by reference. If you change a parameter within a function, the change reflects in the calling function.
However, when we pass literal arguments like strings, numbers, or tuples, they pass by value. This is because they are immutable
*args: when we don't know how many arguments are passed
**kwargs: pass keyworded variable length of arguments to a function, should use it if want to handle named arguments
'''
### identify operators 'is' vs '=='
'''
"== "is for value equality, checks if two has the same value
'is' is for reference equality, checks if two references refer (or point) to the same object, i.e if they're identical
Two objects having equal values are not necessarily identical.
'''
### Python scope
'''
a variable defined inside a function is local to that function, variable defined outside any other scope is global to the function
can read the variable from enclosing scope but cannot make change to it
A namespace is a collection of names. It maps names to corresponding objects.
Builtin, global, enclosing, local
'''
### pickling vs unpickling
'''
for serializing and de-serializing a Python object structure.
Pickling - is the process whereby a Python object hierarchy is converted into a byte stream,
Unpickling - is the inverse operation, whereby a byte stream is converted back into an object hierarchy.
'''
### copy vs deepcopy
'''
A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. In essence, a shallow copy is only one level deep, the copy is not fully independent of the original
A deep copy makes the copying process recursive. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original.
eg xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs). When x append, no effect in ys, but when xs[1][0] = 'X', both will change because of the one level copy
zs = copy.deepcopy(xs), then zs will not change no matter what xs does
'''