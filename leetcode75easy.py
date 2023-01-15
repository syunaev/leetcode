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

def len_of_longest_substring(s):
    """ Given a string s, find the length of the longest
        substring without repeating characters."""
    # https://www.youtube.com/watch?v=qqXOZD4zKEg
    """
    1. start for loop from first char
    2. init empty set
    3. while not exist - increment count
    4. return
    O(N^2)
    """
    result = 0
    for i in range(len(s)):
        seen = set()
        char = i
        counter = 0
        while char < len(s):
            if s[char] not in seen:
                seen.add(s[char])
                counter = counter + 1
                char = char + 1
            else:
                break
        if counter > result:
            result = counter
    return result
