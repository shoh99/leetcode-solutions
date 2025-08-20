"""
Question:
    Given an array nums with n objects colored, red, white, or blue
    sort them in-place so that objects of same color adjacent, with
    the colors in the order red, white, and blue.

    We will use the integers 0,1 and 2 to represent the color red, white, and blue.

    You must solve this problem without using the library's sort function.
"""
from typing import List


def sort_colors(nums: List[int]) -> None:
    for i in range(len(nums)):
        min_num = nums[i]
        min_index = i
        for n in range(i+1, len(nums)):
            if min_num > nums[n]:
                min_num = nums[n]
                min_index = n

        print(f"min value {min_num}, min index: {min_index}")
        nums[min_index] = nums[i]
        nums[i] = min_num

    print(nums)


if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    sort_colors(nums)
