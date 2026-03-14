"""
LeetCode 1415
The k-th Lexicographical String of All Happy Strings of Length n

A happy string is defined as:
1. It only contains characters 'a', 'b', and 'c'
2. No two adjacent characters are the same

Given integers n and k, return the k-th lexicographical happy string of
length n. If there are fewer than k happy strings, return "".

Approach:
Instead of generating all happy strings, we construct the answer
character by character using combinatorics.

Observations:
• First character → 3 choices
• Every next character → 2 choices (cannot repeat previous)

Total happy strings:
3 * 2^(n-1)

At each position we check how many strings are possible with
a candidate character. If k is larger than that count,
we skip that block.
"""


# ------------------------------------------------
# User-Friendly Human Thinking Solution
# ------------------------------------------------

class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        total = 3 * (2 ** (n - 1))

        if k > total:
            return ""

        result = ""
        prev = ""

        for i in range(n):

            for ch in "abc":

                if ch == prev:
                    continue

                count = 2 ** (n - i - 1)

                if k > count:
                    k -= count
                else:
                    result += ch
                    prev = ch
                    break

        return result


"""
Example

Input:
n = 3
k = 9

Total happy strings = 3 * 2² = 12

We skip blocks lexicographically until the correct block
containing the k-th string is found.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""
