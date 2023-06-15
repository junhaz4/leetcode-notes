def subarray_products(numbers,k):
  product = 1
  left = 0
  res = 0
  for right in range(len(numbers)):
    product = product*numbers[right]
    while product > k and left <= right:
      product = product/numbers[left]
      left += 1
    res += right - left + 1
  '''
  n = len(numbers)
  product = 1
  res = 0
  left, right = 0, 0
  while right < n:
    product = product*numbers[right]
    while start < end and product > k:
      p = p/number[left]
      start += 1
    if p <= k:
      res += right-start+1
    right += 1
  '''
  return res

import bisect
def find_LIS(nums):
  '''
  dp = [1] * len(nums)
  for i in range(1, len(nums)):
      for j in range(i):
          if nums[i] > nums[j]:
              dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)
  '''
  
  """
  sub = [nums[0]]
  for num in nums[1:]:
    if num > sub[-1]:
      sub.append(num)
    else:
      i = 0
      while num > sub[i]:
        i += 1
      sub[i] = num
  return len(sub)
"""
  sub = []
  for num in nums:
    i = bisect.bisect_left(sub, num)
      # If num is greater than any element in sub
    if i == len(sub):
        sub.append(num)
      # Otherwise, replace the first element in sub greater than or equal to num
    else:
        sub[i] = num
  return len(sub)


# Heap sort takes O(nlogn) and heap takes O(n) linear time
# stability is more of a concern when dealing with composite data types
# increasing array: remove 4 from the begining and 4, 5 2 from the end
# k-distinct integers: k*k <= n

import math
print(math.trunc(1.99))
print(int(1.99))

import requests
import json

def pulse_rate(name,id):
  url = 'https://jsonmock.hackerrank.com/api/medical_records'
  response = requests.get(url)
  data = json.loads(response.text.encode('utf8'))['data']
  if not data:
    return -1
  url = 'https://jsonmock.hackerrank.com/api/medical_records'
  response = requests.get(url)
  data = json.loads(response.text.encode('utf8'))['data']
  patients = []
  for record in data:
    if record['diagnosis']['name'] == name and record['doctor']['id'] == id:
      patients.append(record['vitals']['pulse'])
  print(patients)
  return sum(patients)/len(patients)

def fit_count(lower,upper):
  url = 'https://jsonmock.hackerrank.com/api/medical_records'
  response = requests.get(url)
  data = json.loads(response.text.encode('utf8'))['data']
  count = 0
  for record in data:
    blood_pressure = record['vitals']['bloodPressureDiastole']
    if lower <= blood_pressure <= upper:
      count += 1
  return count


import requests
import json
from datetime import datetime

def numDevices(statusQuery, threshold, dateStr):
    # Write your code here
    url = 'https://jsonmock.hackerrank.com/api/iot_devices/search?status='+statusQuery
    response = requests.get(url)
    content = json.loads(response.text.encode('utf8'))
    total_pages = content['total_pages']
    date = datetime.strptime(dateStr,'%M-%Y')
    month, year = date.month, date.year
    count = 0
    for i in range(total_pages):
        url = url + "&page=" + str(i)
        response = requests.get(url)
        data = json.loads(response.text.encode('utf8'))['data']
        for record in data:
            dt = record['timestamp']
            time = datetime.fromtimestamp(dt/1000.0)
            time = datetime.utcfromtimestamp(dt//1000).replace(microsecond=dt%1000*1000)
            time = datetime.datetime.fromtimestamp(dt / 1000.0, tz=datetime.timezone.utc)
            if record['operatingParams']['rootThreshold'] > int(threshold) and (time.month == month and time.year == year):
                count += 1
    return count 


# cities with more customers than average
'''
select country_name, city_name, count(customer_name) as NumOfCustomers 
from country join city on country.id = city.country_id 
join customer on city.id = customer.city_id 
where count(customer_name) > (select count(customer_name)/count(city_id) from customer)
group by city_id 
order by country_name asc;

WITH CTE AS(
SELECT DISTINCT CO.country_name, Ci.city_name,COUNT(city_id) AS cnt
, AVG(COUNT(city_id)) OVER() avg_cnt
FROM COUNTRY CO
INNER JOIN City CI ON CI.country_id = CO.id
INNER JOIN Customer CU ON CU.city_id = CI.id
GROUP BY CO.country_name,CI.city_name
)
SELECT country_name,city_name, cnt
FROM CTE WHERE cnt > avg_cnt ORDER BY country_name

SELECT country.country_name, city.city_name, COUNT(customer.id) AS 
num_customer
FROM city
JOIN country ON city.country_id = country.id
JOIN customer ON city.id = customer.city_id
GROUP BY city.id
HAVING num_customer > (SELECT AVG(num_customer) FROM (SELECT city.id, 
COUNT(customer.id) AS num_customer
FROM city
JOIN country ON city.country_id = country.id
JOIN customer ON city.id = customer.city_id
GROUP BY city.id) AS temp)
ORDER BY country.country_name;
'''

'''
def solve(products):
  l = len(products)
  pair = []
  for i, n in enumerate(products):
    pair.append([n,i])
  pair.sort()
  visited = [False]*l
  count = 0
  for i in range(l):
    if visited[pair[i][1]]:
      continue
    count += pair[i][0]
    visited[pair[i][1]] = True
    change_left(visited,pair[i][1],l)
    change_right(visited,pair[i][1],l)
  return count 

def change_left(visited,id,l):
  id -= 1
  while id >= 0:
    if visited[id] == False:
      visited[id] = True
      return 
    else:
      id -= 1
  return 

def change_right(visited,id,l):
  id += 1
  while id < l:
    if visited[id] == False:
      visited[id] = True
      return 
    else:
      id += 1
  return 
  
So, first we store the pairs {w[i],i} in an array(say v) where w[i] represents the weight of ith product and sort it in the ascending order of it's weights (here two items of equal weights will be sorted in such a way that the product with least index comes first).

We also maintain an array(say t) to store the information about the product. t[i] = 0 indicates that the i th product is not picked and t[i]=1 indicates that it is picked. 

Now we traverse the array(v) and for each element we check if it is picked or not. If it is picked, then we continue traversing the array. Else, we add the weight of it to the final answer and mark the adjacent products and itself as picked. 
void mark_left(vector<int> &t, int id, int n)            //marks the immediate left unpicked product as 1
{
    id--;
    while (id >= 0)
    {
        if (t[id] == 0)
        {
            t[id] = 1;
            return;
        }
        else
            id--;
    }
    return;
}
void mark_right(vector<int> &t, int id, int n)             //marks the immediate right unpicked product as 1
{
    id++;
    while (id < n)
    {
        if (t[id] == 0)
        {
            t[id] = 1;
            return;
        }
        else
            id++;
    }
}
int findTotalWeight(vector<int> products) {
    
    int n = products.size();

    vector<pair<int, int>> v;
    for (int i = 0; i < n; i++)
    {
        v.push_back({products[i], i});
    }
    sort(v.begin(), v.end());
    vector<int> t(n);

    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        if (t[v[i].second])
            continue;

        cnt += v[i].first;
        t[v[i].second] = 1;
        mark_left(t, v[i].second, n);
        mark_right(t, v[i].second, n);
    }
    return cnt;
}


'''

# maximum discount product
'''
SELECT PRD.CATEGORY, PRD.PRODUCT_ID, PRD.DISCOUNT
(SELECT P.CATEGORY, MIN(P.PRODUCT_ID) AS 'PID', P.DISCOUNT
FROM PRODUCT AS P
INNER JOIN
(SELECT CATEGORY, MAX(DISCOUNT) AS 'MAXDIS'
FROM PRODUCT 
GROUP BY CATEGORY) AS T
ON P.CATEGORY = T.CATEGORY
AND P.DISCOUNT = T.MAXDIS
GROUP BY P.CATEGORY, P.DISCOUNT) AS PRD
ORDER BY PRD.PRODUCT_ID ASCß
'''

# election
'''
select c.party, count(constitutin_id) as 'Seats_won'
from candidates as c
inner join
(select * from Results
where votes in (
  select max(votes)
  from results as r
  group by constitution_id)) as won
on won.candidate_id = c.id
group by c.party
'''


def solve(products):
  l = len(products)
  pair = []
  for i, n in enumerate(products):
    pair.append([n,i])
  pair.sort()
  visited = [False]*l
  count = 0
  for i in range(l):
    if visited[pair[i][1]]:
      continue
    count += pair[i][0]
    visited[pair[i][1]] = True
    change_left(visited,pair[i][1],l)
    change_right(visited,pair[i][1],l)
  return count 

def change_left(visited,id,l):
  id -= 1
  while id >= 0:
    if visited[id] == False:
      visited[id] = True
      return 
    else:
      id -= 1
  return 

def change_right(visited,id,l):
  id += 1
  while id < l:
    if visited[id] == False:
      visited[id] = True
      return 
    else:
      id += 1
  return 

products = [6,4,9,10,34,56,54]
print(solve(products))