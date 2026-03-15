"""
LeetCode 1622
Fancy Sequence

Design a data structure that supports the following operations:

append(val)   → append an integer to the sequence
addAll(inc)   → add inc to every element
multAll(m)    → multiply every element by m
getIndex(i)   → return the element at index i (mod 1e9+7)

If index i is out of bounds return -1.

Approach:
Updating every element after addAll or multAll would be too slow.
Instead we maintain two global transformations:

value = stored_value * mul + add

Where:
mul → cumulative multiplication factor
add → cumulative addition factor

When inserting a value we reverse the transformation so that
future operations apply correctly.

Reverse transformation:

stored_value = (val - add) * inverse(mul)

This keeps every operation O(1).

Key Idea:
Lazy transformation using modular arithmetic.
"""


# ------------------------------------------------
# Optimized Constant Time Data Structure
# ------------------------------------------------

class Fancy:

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0
        self.mod = 10**9 + 7

    def append(self, val: int) -> None:
        # Reverse transformation before storing
        val = (val - self.add) % self.mod
        val = val * pow(self.mul, -1, self.mod) % self.mod
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod


"""
Example

Operations:
append(2)
addAll(3)
append(7)
multAll(2)

Sequence evolution:
[2]
[5]
[5,7]
[10,14]

getIndex(0) → 10

Time Complexity:
append   → O(1)
addAll   → O(1)
multAll  → O(1)
getIndex → O(1)

Space Complexity:
O(n)
"""
