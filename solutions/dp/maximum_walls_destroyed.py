"""
Custom Problem
Maximum Walls Destroyed by Robots

You are given:
• robots → positions of robots
• distance → how far each robot can destroy walls
• walls → positions of walls

Each robot can destroy walls either:
• to the LEFT
• or to the RIGHT

Goal:
Maximize the number of walls destroyed.

--------------------------------------------------

Human Intuition:

1. First, sort robots based on position.
   This helps us process them from left → right.

2. Some walls are GUARANTEED:
   • If a wall exists exactly at a robot position,
     it will always be destroyed.
   → Count them separately.

3. Remaining walls are "clean walls"
   → We will decide which robot destroys which.

4. DP Strategy:

For each robot, we have 2 choices:
• Destroy LEFT
• Destroy RIGHT

dp[i][0] → max walls if i-th robot goes LEFT
dp[i][1] → max walls if i-th robot goes RIGHT

5. Key Idea:
Avoid double-counting overlapping wall ranges.

We use binary search (bisect) to count walls in ranges efficiently.

--------------------------------------------------

Time Complexity:
O(n log n + w log w)

Space Complexity:
O(n)

--------------------------------------------------
"""

from bisect import bisect_left, bisect_right


class Solution:
    def maximumWallsDestroyed(self, robots: list[int], distance: list[int], walls: list[int]) -> int:

        # Step 1: Sort robots with distances
        robot_data = sorted(zip(robots, distance))
        n = len(robot_data)

        # Step 2: Separate guaranteed walls
        robot_positions = set(robots)
        guaranteed_walls = 0
        clean_walls = []

        for w in sorted(walls):
            if w in robot_positions:
                guaranteed_walls += 1
            else:
                clean_walls.append(w)

        # Step 3: Helper → count walls in range
        def count_in_range(L, R):
            if L > R:
                return 0
            left_idx = bisect_left(clean_walls, L)
            right_idx = bisect_right(clean_walls, R)
            return right_idx - left_idx

        # DP states
        LEFT, RIGHT = 0, 1
        dp = [[0, 0] for _ in range(n)]

        # First robot
        p0, d0 = robot_data[0]
        dp[0][LEFT] = count_in_range(p0 - d0, p0 - 1)
        dp[0][RIGHT] = 0

        # Process robots
        for i in range(1, n):
            p_prev, d_prev = robot_data[i - 1]
            p_curr, d_curr = robot_data[i]

            # Zone between robots
            L_zone = p_prev + 1
            R_zone = p_curr - 1

            # ---- LEFT choice ----
            val0_if_left = dp[i - 1][LEFT] + count_in_range(max(L_zone, p_curr - d_curr), R_zone)

            c1 = count_in_range(L_zone, min(R_zone, p_prev + d_prev))
            c2 = count_in_range(max(L_zone, p_curr - d_curr), R_zone)
            c_intersect = count_in_range(
                max(L_zone, p_curr - d_curr),
                min(R_zone, p_prev + d_prev)
            )

            val1_if_left = dp[i - 1][RIGHT] + (c1 + c2 - c_intersect)

            dp[i][LEFT] = max(val0_if_left, val1_if_left)

            # ---- RIGHT choice ----
            val0_if_right = dp[i - 1][LEFT]

            val1_if_right = dp[i - 1][RIGHT] + count_in_range(
                L_zone,
                min(R_zone, p_prev + d_prev)
            )

            dp[i][RIGHT] = max(val0_if_right, val1_if_right)

        # Last robot
        p_last, d_last = robot_data[-1]

        ans_if_left = dp[-1][LEFT]
        ans_if_right = dp[-1][RIGHT] + count_in_range(p_last + 1, p_last + d_last)

        return guaranteed_walls + max(ans_if_left, ans_if_right)
