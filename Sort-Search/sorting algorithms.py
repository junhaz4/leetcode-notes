# Selection Sort
# time complexity: O(n^2)
# space complexity: O(1)
# stable
"""repeatedly find the index of the minimum element in the unsorted part of the array
and swap it with the first element in the unsorted part of the array."""
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1,len(nums)):
            # Update minimum index
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap current index with minimum element in rest of list
        nums[i], nums[min_index] = nums[min_index], nums[i]


# Bubble Sort
# time complexity: O(n^2) worst case when smallest element is at the end
# space complexity: O(1)
# stable
"""comparing adjacent pairs of elements and swapping them if they are in the wrong order until the list is sorted."""
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
class Solution:
    def bubble_sort(self, lst: list[int]) -> None:
        has_swapped = True
        # if no swap occurred, lst is sorted
        while has_swapped:
            has_swapped = False
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    # Swap adjacent elements
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    has_swapped = True


# Insertion Sort
# time complexity: O(n^2)
# space complexity: O(1)
# Not stable
"""It iterates over the given list, figures out what the correct position of every element is, and inserts it there"""
def insertion_sort(nums):
    for i in range(1,len(nums)):
        current = i
        while current > 0 and nums[current] < nums[current-1]:
            nums[current], nums[current-1] = nums[current-1], nums[current]
            current -= 1



# Heap Sort
# time complexity: O(n log n)
# space complexity: O(1)
# not stable
class Solution:
    def heap_sort(self, lst: list[int]) -> None:
        """
        Mutates elements in lst by utilizing the heap data structure
        """
        def max_heapify(heap_size, index):
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[index], lst[largest] = lst[largest], lst[index]
                max_heapify(heap_size, largest)

        # heapify original lst
        for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(lst), i)

        # use heap to sort elements
        for i in range(len(lst) - 1, 0, -1):
            # swap last element with first element
            lst[i], lst[0] = lst[0], lst[i]
            # note that we reduce the heap size by 1 every iteration
            max_heapify(i, 0)

# Merge Sort
# time complexity: O(n log n)
# space complexity: O(n)
# Stable
"""
It's a recursive divide & conquer algorithm that essentially divides a given list into two halves, sorts those halves, 
and merges them in order. The base case is to merge two lists of size 1, eventually, single elements are merged in order"""
def merge_sort(nums):
    if len(nums) > 1:
        mid  = len(nums) // 2
        # divide the list into 2 halves
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left) # sort the left half
        merge_sort(right) # sort the right half
        i = 0 # index for left half
        j = 0 # index of right half
        k = 0 # index of nums

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        # when either left or right is empty, copy the remaining elements
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


# Quick Sort
# time complexity: O(n^2) when nums is sorted or all elements are equal. Average case is O(n log n)
# space complexity: O(log n)
"""
Steps for quick sort algorithm
1. Start with a list of n elements
2 .Choose a pivot element from the list to be sorted
3. Partition the list into 2 unsorted sublists, such that all elements in one sublist are less than the pivot and all the elements in the other sublist are greater than the pivot
4. Elements that are equal to the pivot can go in either sublist
5. Sort each sublist recursively to yield two sorted sublists
6. Concatenate the two sorted sublists and the pivot to yield one sorted list
Pivot can be choose randomly or choose the last element in the list
"""
def sort_nums(nums):
    quick_sort(nums,0,len(nums)-1)
    return nums

def quick_sort(nums,left,right):
    if left < right:
        pivot = partition(nums,left,right)
        quick_sort(nums,left,pivot-1)
        quick_sort(nums,pivot+1,right)
    else:
        return

def partition(nums,left, right):
    pivot = nums[right]
    i = left
    for j in range(left,right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i



# Bucket Sort
# time complexity: O(n^2) Average case is O(n)
# space complexity: O(n+k)
# stable
def bucket_sort(nums):
    bucket = []
    # Create empty buckets
    for i in range(len(nums)):
        bucket.append([])
    # insert elements in the correct bucket
    for n in nums:
        index = int(10*n)
        bucket[index].append(n)
    # sort each bucket
    for i in range(len(nums)):
        bucket[i] = sorted(bucket[i])
    # concatenate all the buckets
    k = 0
    for i in range(len(nums)):
        for j in range(len(bucket[i])):
            nums[k] = bucket[i][j]
            k += 1
    return nums