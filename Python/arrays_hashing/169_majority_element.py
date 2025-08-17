from typing import List


def majority_element(nums: List[int]) -> int:
    element_dic = dict()
    for num in nums:
        if not element_dic.get(num):
            element_dic[num] = 1
            continue

        element_dic[num] = element_dic.get(num) + 1

    majority_num = 0
    majority_key = 0

    for key in element_dic.keys():
        current_num = element_dic.get(key)
        if current_num > majority_num:
            majority_num = current_num
            majority_key = key

    print(f"Majority number: {majority_key} repeated: {majority_num}")

    return majority_key


def improveved_majority_element(nums: List[int]) -> int:
    """
    :param nums:
    :return: int majority element

    Boyer-Moore Voting Algorithm, and it works in linera time O(n) and constant space O(1).
    Here is the core idea:
    1. Initialize a candidate variable and a count variable (let's start count at 0)
    2. Iterate through the arrays nums.
    3. If count is 0, set the current element as the new candidate.
    4. If the current element is the same as candidate, increment the count.
    5. If the current element is different form the candidate, decrement the count.

    After iterating through the entire array, the candidate will be your majority element.
    """

    candidate = 0
    count = 0

    for i in range(len(nums)):
        current_num = nums[i]
        if i == 0:
            candidate = current_num
            count = 1
            continue

        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
            if count <= 0:
                candidate = current_num
                count = 1

    return candidate


if __name__ == "__main__":
    nums = [1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2]

    res = improveved_majority_element(nums)

    print(res)
