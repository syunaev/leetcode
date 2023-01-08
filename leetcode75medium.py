def three_sum(nums):
    """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    """
    result = []
    # sort the array to use two_sum_two algorithm
    nums.sort()
    for i, a in enumerate(nums):
        # if current element and previous element is the same - skip element
        if i > 0 and a == nums[i - 1]:
            continue
        # find 2 elements using two_sum_two algorithm for sorted arrays and 2 pointers
        left = i + 1
        right = len(nums) - 1
        while left < right:
            # calculate sum - it should be 0 in thi problem but it can be anything
            three_sum = a + nums[left] + nums[right]
            # checking results
            if three_sum > 0: # if results is more than target
                # decreasing right pointer
                right = right - 1
            elif three_sum < 0: # if result is less than target
                # increasing left pointer
                left = left + 1
            else:
                # found one result, add it into the array
                result.append([a, nums[left], nums[right]])
                # increase left pointer
                left = left + 1
                # if there is duplicate in the array increase more
                while nums[left] == nums[left + 1] and left < right:
                    left = left + 1
    return result