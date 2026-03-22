"""
LeetCode 1886
Determine Whether Matrix Can Be Obtained By Rotation

You are given two n x n binary matrices:
• mat
• target

Return True if mat can be rotated in 90° increments
(0°, 90°, 180°, 270°) to match target.

------------------------------------------------

Approach (Human Thinking):

Step 1: Try all 4 rotations
A square matrix has only 4 possible orientations:
    • 0°
    • 90°
    • 180°
    • 270°

Step 2: Check equality
After each rotation:
    if mat == target → return True

Step 3: Perform rotation
To rotate 90° clockwise:
    1. Reverse rows
    2. Take transpose

Python trick:
    zip(*mat[::-1])

------------------------------------------------

Key Insight:

Matrix rotation can be reduced to:
reverse + transpose

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def findRotation(
        self,
        mat: List[List[int]],
        target: List[List[int]]
    ) -> bool:

        # try all 4 rotations
        for _ in range(4):

            if mat == target:
                return True

            # rotate 90° clockwise
            mat = [list(row) for row in zip(*mat[::-1])]

        return False


"""
Example

mat =
[
 [0,1],
 [1,0]
]

target =
[
 [1,0],
 [0,1]
]

Rotate 90°:
[
 [1,0],
 [0,1]
]

→ match found → True

------------------------------------------------

Time Complexity:
O(n²)

Space Complexity:
O(n²)

------------------------------------------------

Note:

Rotation trick:
zip(*mat[::-1]) is a compact and efficient way
to rotate a matrix in Python.
"""
