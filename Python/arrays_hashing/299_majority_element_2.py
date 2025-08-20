"""
Question:
Given an integer array of size n, find all elements that appear more than [n/3] times.

Explanation:
    [n/3] means an element must make up more than 33.3% of the array. This is a weaker condition, and there can be
    at most two such elements.
"""
from typing import List


def majority_elements(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return nums
    elif len(nums) == 0:
        return []

    condition = len(nums) // 3 + 1
    print(f"Condition: {condition}")
    sorted_nums = sorted(nums)

    candidate = 0
    count = 0
    results = []

    for i in range(len(nums)):
        current_num = sorted_nums[i]
        if i == 0:
            candidate = current_num
            count = 1
            continue

        if current_num == candidate:
            count += 1
        else:
            if count >= condition:
                results.append(candidate)

            candidate = current_num
            count = 1

        if i == len(nums) - 1:
            if count >= condition:
                results.append(candidate)

    print(f"Final majority elements: {results}")


def improved_majority_element(nums):
    candidate1 = candidate2 = 0
    count1 = count2 = 0

    for num in nums:
        if count1 == 0 and num != candidate2:
            count1 = 1
            candidate1 = num
        elif count2 == 0 and num != candidate1:
            count2 = 1
            candidate2 = num
        elif candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0,0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    threshold = len(nums) // 3 + 1
    result = []

    if threshold <= count1:
        result.append(candidate1)
    if threshold <= count2:
        result.append(candidate2)

    print(result)


if __name__ == "__main__":
    nums = [2, 1, 1, 3, 1, 4, 5, 6]
    improved_majority_element(nums)
