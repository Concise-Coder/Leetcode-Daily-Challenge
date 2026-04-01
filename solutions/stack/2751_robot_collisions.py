"""
LeetCode 2751
Robot Collisions

You are given:
• positions[i] → position of robot i
• healths[i]   → health of robot i
• directions[i] → 'L' or 'R'

All robots move at the same speed.

Rules:
• When two robots collide:
    - Robot with smaller health dies
    - Robot with larger health loses 1 health
    - If equal → both die

Task:
Return remaining robots' health in original order.

------------------------------------------------

Approach (Human Thinking):

Step 1: Combine robot data

Store:
[position, health, direction, original_index]

------------------------------------------------

Step 2: Sort by position

We process collisions from left → right

------------------------------------------------

Step 3: Use stack

Stack keeps robots moving RIGHT

When a LEFT-moving robot comes:
→ It may collide with stack top

------------------------------------------------

Step 4: Collision simulation

While collision possible:

Case 1:
equal health → both destroyed

Case 2:
stack robot stronger → it survives (health--)

Case 3:
current robot stronger → continue collision

------------------------------------------------

Step 5: Add survivors

If current robot survives → push to stack

------------------------------------------------

Step 6: Restore original order

Sort by original index

------------------------------------------------

Key Insight:

This is similar to:
"Asteroid Collision"

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def survivedRobotsHealths(
        self,
        positions: List[int],
        healths: List[int],
        directions: str
    ) -> List[int]:

        n = len(positions)

        # -------------------------
        # Step 1: Combine data
        # -------------------------
        robots = []

        for i in range(n):
            robots.append([
                positions[i],
                healths[i],
                directions[i],
                i
            ])

        # -------------------------
        # Step 2: Sort by position
        # -------------------------
        robots.sort(key=lambda x: x[0])

        stack = []

        # -------------------------
        # Step 3: Process collisions
        # -------------------------
        for robot in robots:

            if robot[2] == 'R':
                stack.append(robot)

            else:
                # moving LEFT → may collide
                while (
                    stack and
                    stack[-1][2] == 'R' and
                    robot[1] > 0
                ):

                    top_robot = stack[-1]

                    # equal health → both die
                    if top_robot[1] == robot[1]:
                        stack.pop()
                        robot[1] = 0

                    # stack robot stronger
                    elif top_robot[1] > robot[1]:
                        top_robot[1] -= 1
                        robot[1] = 0

                    # current robot stronger
                    else:
                        stack.pop()
                        robot[1] -= 1

                # if still alive → add to stack
                if robot[1] > 0:
                    stack.append(robot)

        # -------------------------
        # Step 4: Restore order
        # -------------------------
        stack.sort(key=lambda x: x[3])

        return [robot[1] for robot in stack]


"""
Example

positions = [1,2,3]
healths  = [5,3,4]
dirs     = "RLL"

Collisions happen between adjacent robots
based on directions.

------------------------------------------------

Time Complexity:
O(n log n)  (sorting)

Space Complexity:
O(n)

------------------------------------------------

Key Patterns:

• Stack simulation
• Collision handling
• Sorting + original index tracking

------------------------------------------------

Important Insight:

Whenever you see:
"objects moving + collisions"
→ Think stack simulation
"""
