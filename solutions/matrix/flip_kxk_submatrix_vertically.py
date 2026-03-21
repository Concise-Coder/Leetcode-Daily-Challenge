"""
LeetCode (Custom / Utility Problem)
Flip k x k Submatrix Vertically

You are given a grid and parameters:
• (x, y) → top-left corner of submatrix
• k → size of square submatrix

Task:
Flip the k x k submatrix vertically.

That means:
• First row swaps with last row
• Second row swaps with second last row
• and so on...

------------------------------------------------

Approach (Human Thinking):

Step 1: Identify rows to swap
We only need to process half of the rows:
    range(k // 2)

Step 2: Compute indices
Top row:
    x + i
Bottom row:
    x + k - 1 - i

Step 3: Swap elements column-wise
For each column in range(y → y+k):
    swap elements of top row and bottom row

------------------------------------------------

Key Insight:

Vertical flip = row reversal within the submatrix

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def flipRowVertical(
        self,
        grid: List[List[int]],
        x: int,
        y: int,
        k: int
    ) -> List[List[int]]:

        # iterate only half rows
        for i in range(k // 2):

            top_row = x + i
            bottom_row = x + k - 1 - i

            # swap row segments
            for j in range(y, y + k):
                grid[top_row][j], grid[bottom_row][j] = (
                    grid[bottom_row][j],
                    grid[top_row][j]
                )

        return grid


"""
Example

grid =
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

x = 0, y = 0, k = 3

Submatrix:
[1,2,3]
[4,5,6]
[7,8,9]

After vertical flip:
[7,8,9]
[4,5,6]
[1,2,3]

------------------------------------------------

Time Complexity:
O(k²)

Space Complexity:
O(1)

------------------------------------------------

Note:

This is an in-place operation.
No extra memory is used.

Useful in:
• Matrix transformations
• Image processing
• Simulation problems
"""
