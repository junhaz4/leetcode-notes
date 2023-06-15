# method 1: bubble sort
def sort_binary_list(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# method 2: swaps
def sort_binary_array(nums):
    left, right = 0, len(nums)-1
    while left < right:
        while left < right and nums[left] != 1: # find 1 from the left
            left += 1
        while left < right and nums[right] != 0: # find 0 from right
            right -= 1
        nums[left], nums[right] = nums[right], nums[left] # swap
    return nums

nums = [1,0,1,0,1,1,0,0]
print(sort_binary_array(nums))

# method 3
def sort_binary_nums(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """

    j = 0

    for i in range(len(lst)):
        if lst[i] < 1:  # Swapping with jth element if the number is less than 1
            lst[i], lst[j] = lst[j], lst[i]  # Swapping
            j = j + 1

    return lst