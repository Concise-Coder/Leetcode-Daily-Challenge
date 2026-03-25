"""
LeetCode (Grid Partition Problem)
Check if Grid Can Be Partitioned Into Two Equal Sum Parts

You are given a 2D grid of integers.

Task:
Check if we can split the grid into two parts such that:
• The sum of both parts is equal
• Split must be:
    - Horizontal (between rows)
    OR
    - Vertical (between columns)

------------------------------------------------

Approach (Human Thinking):

Step 1: Compute total sum
If total sum is odd → impossible → return False

------------------------------------------------

Step 2: Target sum
We need each part to have:
    target = total_sum // 2

------------------------------------------------

Step 3: Try horizontal splits

Accumulate row sums:
    keep adding row by row

If at any point:
    current_sum == target → return True

------------------------------------------------

Step 4: Try vertical splits

Accumulate column sums:
    sum(grid[i][j] for i in range(m))

If:
    current_sum == target → return True

------------------------------------------------

Key Insight:

We only need to check prefix partitions
(not all submatrices)

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        m, n = len(grid), len(grid[0])

        total_sum = sum(sum(row) for row in grid)

        # if total sum is odd → cannot split
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # -------------------------
        # Horizontal split
        # -------------------------
        current_sum = 0

        for i in range(m - 1):
            current_sum += sum(grid[i])

            if current_sum == target:
                return True

        # -------------------------
        # Vertical split
        # -------------------------
        current_sum = 0

        for j in range(n - 1):
            current_sum += sum(grid[i][j] for i in range(m))

            if current_sum == target:
                return True

        return False


"""
Example

grid =
[
 [1,1],
 [1,1]
]

Total sum = 4 → target = 2

Horizontal:
[1,1] → sum = 2 → valid

------------------------------------------------

Time Complexity:
O(m * n)

Space Complexity:
O(1)

------------------------------------------------

Key Pattern:

Prefix sum over rows and columns

------------------------------------------------

Note:

Only straight cuts allowed:
• horizontal OR vertical
"""
