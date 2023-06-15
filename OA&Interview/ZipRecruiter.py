from audioop import add
from pickle import TRUE


def add_even_odd(num):
  odd_sum = 0
  even_sum = 0
  if num % 2 == 1:
    is_odd = True
  else:
    is_odd = False
  while num != 0:
    if is_odd:
      odd_sum += num%10
    else:
      even_sum += num%10
    is_odd = not is_odd
    num = num//10
  return max(even_sum,odd_sum)
#print(add_even_odd(457892))

def merge_digits(num):
  n = len(num)
  start = 0
  res = ''
  while start < n:
    end = start
    count = 1
    while num[end] == num[end+1]:
      count += 1
      end += 1
    res += str(count*int(num[start]))
    start = end+1
    res += num[start]
    start += 1
    
def sum_new(nums):
  res = 0
  for num in nums:
    for n in nums:
      res += int(str(num)+str(n))
  return res
#print(sum_new([2,10,3]))

def find_light_cover(lights,num):
  res = [0]*len(num)
  for i,n in enumerate(num):
    for l in lights:
      if l[0] > n or l[1] < n:
        continue
      if l[0] <= n <= l[1]:
        res[i] += 1
  return res
#print(find_light_cover([[4,7],[5,6],[1,3]],[2,5]))

  
from math import radians, cos, sin, asin, sqrt
def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)
     
     
# driver code
lat1 = 40.795891077617156
lat2 = 42.35871061219057
lon1 = -73.9742053832675
lon2 =  -71.05473364877167
dis = distance(lat1, lat2, lon1, lon2)
speed = 2*(10**8)
time = dis*2*1000/speed*1000
print(time)