# You must implement a function that returns the difference between the biggest and the smallest value in a list(lst) received as parameter.

# The list(list_nums) contains integers, which means it may contain some negative numbers.

# If the list is empty or contains a single element, return 0.

# The list(list_nums) is not sorted.

# solution([1, 2, 3, 4])   return 3, because 4 - 1 == 3
# solution([1, 2, 3, -4])   return 7, because 3 - (-4) == 7

def solution(list_nums):
    # write your code here
    if not list_nums:
        return 0
    current_min = list_nums[0]
    current_max = list_nums[0]
    for num in list_nums:
        if num > current_max:
            current_max = num
        if num < current_min:
            current_min = num
    return current_max - current_min
# print(solution([1, 2, 3, 4]))