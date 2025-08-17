

def countSubarrays(nums, k):
    left = 0
    current_sum = 0
    count = 0

    for i in range(len(nums) -1):
        right = i
        current_sum += nums[right]

        while current_sum * (right - left + 1) >= k:
            nums[left]




if __name__ == "__main__":
    nums = [2,1,4,3,5];
    k = 10

    countSubarrays(nums, k)
