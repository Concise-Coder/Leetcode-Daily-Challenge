"""
LeetCode 3296
Minimum Number of Seconds to Make Mountain Height Zero

Problem:
You are given a mountain with height 'mountainHeight' and a list
'workerTimes'.

Worker i requires workerTimes[i] seconds to remove the first unit of height,
2 * workerTimes[i] seconds for the second unit,
3 * workerTimes[i] seconds for the third unit, etc.

If a worker removes k units of height, the total time taken is:

workerTimes[i] * (1 + 2 + ... + k)
= workerTimes[i] * k * (k + 1) / 2

All workers work simultaneously.

Goal:
Return the minimum number of seconds required to reduce the mountain height to zero.

Approach:
Binary Search on time.

For a given time T:
Determine how many units each worker can remove using the inequality:

workerTimes[i] * k*(k+1)/2 ≤ T

Solve for k and sum contributions from all workers.

If total ≥ mountainHeight → time is feasible.

Time Complexity:
O(n log T)

Space Complexity:
O(1)
"""

from typing import List
import math


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def can_finish(time):

            total_removed = 0

            for w in workerTimes:

                # solve w * k*(k+1)/2 <= time
                val = (2 * time) // w
                k = int((math.sqrt(1 + 4 * val) - 1) // 2)

                total_removed += k

                if total_removed >= mountainHeight:
                    return True

            return False


        left = 0
        right = 10**18
        ans = right

        while left <= right:

            mid = (left + right) // 2

            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
