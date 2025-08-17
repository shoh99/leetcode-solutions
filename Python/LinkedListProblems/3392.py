def countSubarrays(nums):
    sub_array = []
    result = 0

    for i in range(len(nums)):
        if len(sub_array) < 3:
            sub_array.append(nums[i])


        if len(sub_array) == 3:
            first = sub_array[0]
            mid = sub_array[1]
            last = sub_array[-1]

            print(f"first: {first}")
            print(f"mid: {mid}")
            print(f"last: {last}")
            print(f"sum of first and last {first+last}")
            print(f"half of mid: {mid // 2}")

            if mid % 2 == 0 and first + last == mid // 2:
                result += 1

            sub_array = [mid, last]

    print(result)


if __name__ == "__main__":
    nums = [1,1,1]

    countSubarrays(nums)
