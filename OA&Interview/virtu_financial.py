# lc 66, 987, 54, 0/1 knapsack


# lc 1196
def max_number_apples(apples,capacity):
  count = 0
  weight = 0
  apples.sort()
  n = len(apples)
  for i in range(n):
    if weight + apples[i] <= capacity:
      weight += apples[i]
      count += 1
    else:
      break
  return count 
      
# lc 1271
def hexspeak(num):
  mapping = {0: "O", 1: "I", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
  result = ""
  while int(num):
      num, digit = divmod(int(num),16)
      if digit in mapping:
          result = mapping[digit] + result
      else:
          return "ERROR"
  return result
'''
num = int(num)
res = ''
while num > 0:
    num, cur = divmod(num, 16)
    if 2 <= cur <= 9: return 'ERROR'
    if cur == 0: res += 'O'
    elif cur == 1: res += 'I'
    else: res += chr(cur - 10 + ord('A'))
return res[::-1]
'''
import requests