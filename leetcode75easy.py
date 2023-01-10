def two_sum(nums, target):
    """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
    """
    values = {}  # value : index
    for i in range(len(nums)):
        second_value = target - nums[i]
        if second_value in values:
            return [values.get(second_value), i]
        values[nums[i]] = i


def runningSum(nums: List[int]) -> List[int]:
    """
    https://leetcode.com/problems/running-sum-of-1d-array/
    :param nums:
    :return:
    """
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(result[i - 1] + nums[i])

    return result

