from typing import List


def maxTaskAssign(tasks: List[int], workers: List[int], pills: int, strength: int):
    sorted_workers = sorted(workers, reverse=True)
    sorted_tasks = sorted(tasks, reverse=True)
    total = 0
    sorted_task_length = len(sorted_tasks)

    for i in range(len(sorted_workers)):
        worker = sorted_workers[i]
        if sorted_task_length < i+1:
            return total

        task = sorted_tasks[i]

        if worker >= task:
            total += 1

        elif pills >= 1:
            if worker + strength >= task:
                total += 1
                pills -= 1

    return total


if __name__ == "__main__":
    task = [5,9,8,5,9]
    workers = [1,6,4,2,6]
    pills = 1
    strength = 5

    print(maxTaskAssign(task, workers, pills, strength))
