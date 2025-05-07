from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited_time = [[float('inf')] * m for _ in range(n)]

        heap = [(0, 0, 0)]  # (time, row, col)
        visited_time[0][0] = 0

        while heap:
            time, i, j = heapq.heappop(heap)

            if (i, j) == (n - 1, m - 1):
                return time

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    wait_until = max(time, moveTime[ni][nj])
                    next_time = wait_until + 1
                    if next_time < visited_time[ni][nj]:
                        visited_time[ni][nj] = next_time
                        heapq.heappush(heap, (next_time, ni, nj))

        return -1  # Should not reach here as per problem constraints
