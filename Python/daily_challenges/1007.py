from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        print(f"tops length: {len(tops)}")
        print(f"bottoms length: {len(bottoms)}")

        most_rep_num_tops = self._mostReatedNumber(tops)
        most_rep_num_bottoms = self._mostReatedNumber(bottoms)

        swap_to = tops
        swap_from = bottoms

        if most_rep_num_tops["num_of_reps"] >= most_rep_num_bottoms["num_of_reps"]:
            swap_num = most_rep_num_tops["most_rep_num"]
            most_reps = most_rep_num_tops["num_of_reps"]
        else:
            swap_num = most_rep_num_bottoms["most_rep_num"]
            most_reps = most_rep_num_bottoms["num_of_reps"]

            swap_to = bottoms
            swap_from = tops

        print(f"Most swap num: {swap_num} repeated times: {most_reps}")
        print(f"Swap side: {swap_to}")

        total = self._itarateDominos(swap_to, swap_from, swap_num)

        print(f"Minimum swap: {total}")
        if total + most_reps == len(swap_to):
            return total
        else:
            return -1

    def _itarateDominos(self, swap_to_nums, swap_from_nums, swap_num):
        total = 0
        for i in range(len(swap_to_nums)):
            swap_to_i = swap_to_nums[i]
            swap_from_i = swap_from_nums[i]

            if (swap_to_i != swap_num) and (swap_from_i == swap_num):
                total += 1

        return total

    def _mostReatedNumber(self, nums):
        storage = {}

        for i in nums:
            if storage.get(i):
                storage[i] = storage[i] + 1
                continue

            storage[i] = 1

        most_num = {
            "most_rep_num": 0,
            "num_of_reps": 0
        }

        num = 0
        key = 0
        print(storage)
        for i in storage.keys():
            if storage[i] >= num:
                num = storage[i]
                key = i

        most_num["most_rep_num"] = key
        most_num["num_of_reps"] = num

        return most_num


if __name__ == "__main__":
    tops = [2, 2, 2, 4, 4, 4]
    bottoms = [4, 4, 4, 2, 3, 2]

    prob = Solution()
    prob.minDominoRotations(tops, bottoms)
