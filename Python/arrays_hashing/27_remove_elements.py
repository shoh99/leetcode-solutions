from typing import List


def removeElement(nums: List[int], val: int) -> int:
    idx = 0
    while len(nums) > idx:
        current_num = nums[idx]
        if current_num == val:
            nums.pop(idx)
            continue

        idx += 1

    return len(nums)


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    removeElement(nums, val)
