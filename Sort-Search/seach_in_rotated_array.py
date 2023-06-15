def pivot_binary_search(lst,n,key):
    left, right = 0, n-1
    pivot = find_pivot(lst,left,right)
    if pivot == -1:
        return binary_search(lst,left,right,key)
    if lst[pivot] == key:
        return pivot
    if lst[0] < key:
        return binary_search(lst,left,pivot-1,key)
    else:
        return binary_search(lst,pivot+1,right,key)

def find_pivot(lst,left,right):
    # elements before pivot are sorted and elements after pivot are sorted
    if right < left:
        return -1
    if left == right:
        return left
    while left < right:
        mid = left + (right-left)//2
        if mid < right and lst[mid] > lst[mid+1]:
            return mid
        if mid > left and lst[mid] < lst[mid-1]:
            return mid-1
        if lst[left] >= lst[mid]:
            right = mid-1
        else:
            left = mid+1

def binary_search(lst,left,right,key):
    if right < left:
        return -1
    while left <= right:
        mid = left + (right-left)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            right = mid - 1
        else:
            left = mid  + 1

lst = [6, 7, 8, 9, 10, 0, 1, 2, 3]
key = 0
n = len(lst)
print(pivot_binary_search(lst,n,key))

# time complexity: O(log n) both binray search and find pivot functions take this time
# space complexity: O(1)
