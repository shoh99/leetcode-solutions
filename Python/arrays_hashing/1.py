from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    res = []

    i = 0
    while i < len(nums):
        current_num = nums[i]
        for j in range(i+1, len(nums)):
            if current_num + nums[j] == target:
                res.append(i)
                res.append(j)
                break

        i += 1

    return res


def twoSumMap(nums: List[int], target: int) -> List[int]:
    indices = {}

    for i, n in enumerate(nums):
        indices[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indices and indices[diff] != i:
            return [i, indices[diff]]


if __name__ == "__main__":
    nums = [3, 2, 3]

    target = 6
    print(twoSumMap(nums, target))
