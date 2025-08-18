"""
Question:
Given an array of numbers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the space complexity possible.
"""
from typing import List


def sort_array_brute_force(nums: List[int]) -> List[int]:
    """
    Time complexity:
        * min(nums): To find the minimum element in a list of size k, Python has to look at every single
        one of the k elements. This is an O(k) operation.
        * nums.remove(min_num): To remove an element. Python first has to find it (which can take up to k
            steps) and then remove it (which can involve shifting all subsequent elements).
            This is also an O(k) operation.

        For loop runs n times, The size of nums starts at n , then becomes n-1, n-2, and so on.
        On average, the oprations, inside the loop taje about O(n) time.
        Since it performs an O(n) operation inside a loop that runs n times, the total complexity is
        n x O(n) = O(n^2).
    Space Complexity
        It creates a new list, sorted_array, to store the result. This new list will eventually
        hold n elements.

        Therefore, this solution uses (O(n)) extra space.

    :param nums:
    :return:
    """
    sorted_array = []

    for i in range(len(nums)):
        min_num = min(nums)
        sorted_array.append(min_num)
        nums.remove(min_num)

    return sorted_array


def in_place_selection_sort(nums):
    """
    Code Breakdown:
        1. The i loop iterates from 0 to len(nums), setting up the boundary between the
            sorted part on the left and the unsorted part on the right.
        2. Initializing absolute_min_index = i is the key. You start by assuming the first element
            of the unsorted section is the smallest.
        3. The n loop then challenges the assumption by checking every other element in the unsorted
            section. If it finds a smaller one, it updates absolute_min_index.
        4. The swap at the end is the crucial step. After the inner loop has finished, you are guaranteed to
            have the index of the absolute minimum element in the unsorted part. You then swap it
            with nums[i] to lock it into its correct, sorted position.

    Final Complexity Score
        * Time Complexity: O(n^2) - Nested loop, which is the classic signature of this complexity class.
            Perfect for a brute-force approach.
        * Space Complexity: O(1) - This is the big win! By modifying the array in-place and only using a few variables.

    :param nums:
    :return:
    """
    for i in range(len(nums)):
        print(f"Outer loop value: {nums[i]} index: {i}")
        absolute_min = nums[i]
        absolute_min_index = i

        for n in range(i + 1, len(nums)):
            if nums[n] < absolute_min:
                absolute_min = nums[n]
                absolute_min_index = n

        nums[absolute_min_index] = nums[i]
        nums[i] = absolute_min
        print(f"Absolute min value: {absolute_min} at index: {absolute_min_index}")

    print(nums)


def merge_sort(nums):
    # base case : if the array has 0 or 1 elements, its already sorted.
    if len(nums) <= 1:
        return nums

    # 1. Divide: Find the middle and split the array into two halves
    mid_index = len(nums)//2
    left_half = nums[:mid_index]
    right_half = nums[mid_index:]

    # 2. Conquer: Recursively call merge_sort on each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # 3. Combine: Merge the now-sorted halves back together.
    # This ues the helper function
    return merge(sorted_left, sorted_right)




def merge(left_half, right_half):
    result = []
    i = 0  # pointer for left half
    j = 0  # pointer for the right half

    # loop while both pointers are within their array's bounds
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1  # move the left pointer
        else:
            result.append(right_half[j])
            j += 1  # move the right pointer

    # append any remaining elements from the left half
    while i < len(left_half):
        result.append(left_half[i])
        i += 1

    while j < len(right_half):
        result.append(right_half[j])
        j += 1

    return result


if __name__ == "__main__":
    nums = [5,1,1,2,0,0]
    print(merge_sort(nums))

