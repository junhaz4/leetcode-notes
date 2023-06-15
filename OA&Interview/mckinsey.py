def calculateAmount(prices):
  res = prices[0]
  min_price = prices[0]
  for i in range(1,len(prices)):
    if prices[i] - min_price > 0:
      res += prices[i] - prices[i-1]
    else:
      res += max(0, prices[i]-min_price)
    min_price = min(min_price,prices[i])
  return res 

#print(calculateAmount([2,5,1,4]))


def findsmallestdivisor(s,t):
  if len(s) < len(t):
    return -1
  fits = False
  concat = t
  i=1
  while len(concat)<=len(s):
      if concat!=s:
          i+=1
          concat = t * i
      else:
          fits = True
          break
  if not fits:
      return -1
  for i in range(1,len(t)+1):
      if (t[:i]*(len(t)//i)) == t:
          return i
#print(findsmallestdivisor("bcdbcdbcdbcd","bcdbcd"))

'''
SELECT CONCAT(first_name, ' ', last_name) AS Name FROM test.student
mysql> SELECT 'My' 'S' 'QL';
        -> 'MySQL'
select 
 'Student ' || id || ' has grade: ' || 
 CASE 
    WHEN max_grade < 20 then 'F' 
    WHEN max_grade < 40 then 'D'
    WHEN max_grade < 60 then 'C'
    WHEN max_grade < 80 then 'B'
    ELSE 'A'
  END AS Grade_details 
FROM students 
ORDER BY id AESC;
'''

def maximum_index(steps,bad):
  max_index = 0
  for i in range(1,steps+1):
    max_index += i
  cur_index = max_index
  step = steps
  while True:
    while cur_index > 0 and steps > 0:
      cur_index -= steps
      if cur_index == bad:
        cur_index += steps
      steps -= 1
    if cur_index <= 0:
      return max_index
    else:
      steps = step
      cur_index = max_index - 1
      max_index -= 1
      if cur_index == bad:
        cur_index = max_index - 1
        max_index -= 1
        
print(maximum_index(4,6))


import requests
import json

def get_code(name,number):
  url = 'https://jsonmock.hackerrank.com/api/countrie?name=' + str(name)
  response = requests.get(url)
  data = json.loads(response.text.encode('utf8'))['data']
  #data = json.loads(response.content)['data']
  if not data:
    return -1
  


