"""
LeetCode (Advanced Grid Partition Problem)
Check if Grid Can Be Partitioned Into Two Equal Sum Parts (With One Removal)

You are given a 2D grid.

Task:
Check if the grid can be split into two parts such that:
• Sum of both parts is equal
• You are allowed to remove AT MOST one cell from one part

Allowed splits:
• Horizontal
• Vertical
• Also consider reversed orientations

------------------------------------------------

Approach (Human Thinking):

Step 1: Compute total sum

------------------------------------------------

Step 2: Try partitioning

We simulate splitting the grid row by row:

For each split:
    top_sum = sum of upper part
    bottom_sum = remaining sum

diff = top_sum - bottom_sum

------------------------------------------------

Step 3: Cases

Case 1:
    diff == 0
    → already balanced → return True

Case 2:
    diff > 0
    → need to remove value = diff from top section

We check:
• If diff exists in current section

Special optimization:
• Corners can always be removed safely
• If submatrix size ≥ 2x2 → any cell can be removed

------------------------------------------------

Step 4: Try all orientations

We check:
• original grid
• reversed grid
• transposed grid
• reversed transpose

------------------------------------------------

Key Insight:

Instead of checking all submatrices,
we reduce problem using:
prefix sums + set lookup + symmetry

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        total_sum = sum(sum(row) for row in grid)

        def canPartition(g: List[List[int]]) -> bool:

            top_sum = 0
            seen = set()
            cols = len(g[0])

            for i in range(len(g) - 1):

                row = g[i]
                top_sum += sum(row)
                bot_sum = total_sum - top_sum

                seen.update(row)

                diff = top_sum - bot_sum

                # already balanced
                if diff == 0:
                    return True

                if diff > 0:

                    # corner removals (always safe)
                    if diff in (
                        g[0][0],
                        g[0][-1],
                        row[0],
                        row[-1]
                    ):
                        return True

                    # general case (2x2 or larger)
                    if i > 0 and cols > 1:
                        if diff in seen:
                            return True

            return False

        # transpose helper
        def transpose(g: List[List[int]]) -> List[List[int]]:
            return [list(col) for col in zip(*g)]

        return (
            canPartition(grid) or
            canPartition(grid[::-1]) or
            canPartition(transpose(grid)) or
            canPartition(transpose(grid)[::-1])
        )


"""
Example

grid =
[
 [1,2],
 [3,4]
]

Total = 10

We try splits and check if removing one element
can balance the partition.

------------------------------------------------

Time Complexity:
O(m * n)

Space Complexity:
O(n)

------------------------------------------------

Key Patterns:

• Prefix sum partition
• Hash set lookup
• Matrix symmetry (reverse + transpose)

------------------------------------------------

Important Insight:

Checking all orientations avoids writing
separate logic for vertical and reverse splits.
"""
