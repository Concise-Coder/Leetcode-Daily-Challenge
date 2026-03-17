"""
LeetCode 1727
Largest Submatrix With Rearrangements

You are given a binary matrix.

You can rearrange the columns of each row in any order.

Return the area of the largest submatrix consisting only of 1s.

Approach (Human Thinking):

Step 1: Build heights
Think of each column as a histogram.
For every cell:
    if grid[i][j] == 1:
        height[j] += 1
    else:
        height[j] = 0

So each row becomes a histogram of consecutive 1s ending at that row.

Step 2: Rearrangement trick
Since we can rearrange columns, we can sort heights in descending order.

This is the key idea:
We don't care about original column order anymore.

Step 3: Compute area
After sorting:
For each position j:
    area = height[j] * (j + 1)

Why?
Because we can take first (j+1) columns (largest heights).

Step 4: Track maximum area
Do this for every row.

Key Insight:
Sorting allows us to simulate the best possible column arrangement.
"""


# ------------------------------------------------
# Human Thinking Solution
# ------------------------------------------------

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        ans = 0

        for i in range(m):

            # build histogram heights
            for j in range(n):
                if matrix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            # rearrange columns (sort heights descending)
            sorted_heights = sorted(height, reverse=True)

            # calculate max area
            for j in range(n):
                ans = max(ans, sorted_heights[j] * (j + 1))

        return ans


"""
Example

matrix =
[
 [0,0,1],
 [1,1,1],
 [1,0,1]
]

Row-wise heights:
[0,0,1]
[1,1,2]
[2,0,3]

After sorting each row:
[1,0,0]
[2,1,1]
[3,2,0]

Max area = 4

Time Complexity:
O(m * n log n)

Space Complexity:
O(n)
"""
