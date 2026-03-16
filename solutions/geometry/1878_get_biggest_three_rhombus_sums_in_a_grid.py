"""
LeetCode 1878
Get Biggest Three Rhombus Sums in a Grid

You are given an m x n integer matrix grid.

A rhombus sum is defined as the sum of the values of the cells forming
the border of a rhombus shape in the grid.

Return the three largest distinct rhombus sums in descending order.
If there are fewer than three distinct values, return all of them.

Approach:
We iterate over every cell as a possible center of a rhombus.

For each center we try increasing rhombus "radius".
A radius r rhombus has four edges of length r.

Border traversal pattern:
top -> right -> bottom -> left -> top

For each rhombus we compute the border sum and store it in a set
to keep only distinct values.

Finally we return the largest three sums.

Key Observation:
A rhombus with radius r exists only if all four corners remain inside
the grid boundaries.
"""


# ------------------------------------------------
# Brute Force Border Traversal Solution
# ------------------------------------------------

from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])
        values = set()

        for i in range(m):
            for j in range(n):

                # radius = 0 (single cell rhombus)
                values.add(grid[i][j])

                r = 1

                while True:

                    if i-r < 0 or i+r >= m or j-r < 0 or j+r >= n:
                        break

                    s = 0

                    # top -> right
                    x, y = i-r, j
                    for k in range(r):
                        s += grid[x+k][y+k]

                    # right -> bottom
                    x, y = i, j+r
                    for k in range(r):
                        s += grid[x+k][y-k]

                    # bottom -> left
                    x, y = i+r, j
                    for k in range(r):
                        s += grid[x-k][y-k]

                    # left -> top
                    x, y = i, j-r
                    for k in range(r):
                        s += grid[x-k][y+k]

                    values.add(s)

                    r += 1

        return sorted(values, reverse=True)[:3]


"""
Example

grid =
[[3,4,5],
 [3,3,4],
 [20,30,200]]

Possible rhombus border sums are computed and stored.
The three largest distinct values are returned.

Time Complexity:
O(m * n * min(m,n))

Space Complexity:
O(number of rhombus sums)
"""
