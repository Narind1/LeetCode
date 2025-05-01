from collections import deque
from bisect import bisect_right
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k: int) -> bool:
            task_deque = deque(tasks[:k])  # k easiest tasks
            available_workers = workers[-k:]  # k strongest workers
            pills_left = pills

            for i in reversed(range(k)):
                if available_workers[i] >= task_deque[-1]:
                    task_deque.pop()
                else:
                    if pills_left == 0:
                        return False
                    # Look for weakest worker who can do the hardest remaining task with a pill
                    found = False
                    for j in range(i + 1):
                        if available_workers[j] + strength >= task_deque[-1]:
                            available_workers.pop(j)
                            task_deque.pop()
                            pills_left -= 1
                            found = True
                            break
                    if not found:
                        return False
            return True

        low, high = 0, min(len(tasks), len(workers))
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
