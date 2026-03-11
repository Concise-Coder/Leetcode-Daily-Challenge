"""
LeetCode 1009
Complement of Base 10 Integer

Given an integer n, return the bitwise complement of its binary representation.
"""


# ------------------------------------------------
# User Solution
# ------------------------------------------------

class SolutionUser:
    def bitwiseComplement(self, n: int) -> int:
        return int(bin(n)[2:].translate(str.maketrans('01', '10')), 2)


"""
Idea:
1. Convert number to binary using bin().
2. Remove the '0b' prefix.
3. Swap 0 -> 1 and 1 -> 0 using translate().
4. Convert the result back to integer.
"""


# ------------------------------------------------
# Optimized Bit Manipulation Solution
# ------------------------------------------------

class Solution:
    def bitwiseComplement(self, n: int) -> int:

        if n == 0:
            return 1

        mask = 1

        # create mask like 111... (same length as n)
        while mask <= n:
            mask <<= 1

        mask -= 1

        return mask ^ n


"""
Optimized Approach

Example:
n = 5

Binary:
5  = 101

Mask:
111

Complement:
101 XOR 111 = 010 -> 2

Steps:
1. Build a mask of all 1s with same bit length as n.
2. XOR the mask with n to flip the bits.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
