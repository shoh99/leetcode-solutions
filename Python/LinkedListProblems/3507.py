
# 3507. Minimum Pair Removal to Sort Array 1
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False

    return True

def minimum_pair_removal(nums):
    count = 0

    while not is_sorted(nums):
        min_sum = float('inf')
        min_index = 1
        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]
            if current_sum < min_sum:
                min_sum = current_sum
                min_index = i

        if min_index != -1:
            nums[min_index] = nums[min_index] + nums[min_index + 1]
            nums.pop(min_index + 1)
            count += 1

    print(count)



if __name__ == "__main__":
    nums = [5,2,3,1]
    minimum_pair_removal(nums)
