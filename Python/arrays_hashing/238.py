from typing import List
from math import prod


def product_except_self(nums: List[int]) -> List[int]:
    result = []
    m = {}

    for i, v in enumerate(nums):
        if m.get(v):
            result.append(m.get(v))
        else:
            res = prod(nums[0:i]) * prod(nums[i + 1: len(nums)])
            m[v] = res
            result.append(res)

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    res = product_except_self(nums)
    print(res)
