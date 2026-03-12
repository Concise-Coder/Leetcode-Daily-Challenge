"""
LeetCode 3600
Maximize Spanning Tree Stability with Upgrades

Problem:
We must construct a spanning tree of n nodes maximizing the minimum
edge stability.

Each edge has:
u, v  -> endpoints
s     -> stability
must  -> 1 if the edge must be included

Optional edges may be upgraded (stability * 2) up to k times.

Approach:
Binary Search + Union-Find (Disjoint Set Union).

1. Binary search the answer (minimum stability).
2. For a candidate stability x:
   • Include all mandatory edges first.
   • Add optional edges greedily using strongest edges first.
   • If an edge doesn't satisfy stability but doubling does,
     we may upgrade it if upgrades remain.
3. If we can build a spanning tree using ≤ k upgrades,
   the stability is feasible.

Time Complexity:
O(E log E log S)

E = number of edges
S = maximum stability value
"""

from typing import List


# ------------------------------------------------
# Disjoint Set Union (Union-Find)
# ------------------------------------------------

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa

        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1

        return True


# ------------------------------------------------
# Solution
# ------------------------------------------------

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can(x):

            dsu = DSU(n)
            used = 0
            upgrades = 0

            mandatory = []
            optional = []

            for u, v, s, must in edges:
                if must:
                    mandatory.append((u, v, s))
                else:
                    optional.append((u, v, s))

            # process mandatory edges
            for u, v, s in mandatory:
                if s < x:
                    return False

                if not dsu.union(u, v):
                    return False

                used += 1

            # sort optional edges by stability
            optional.sort(key=lambda e: e[2], reverse=True)

            for u, v, s in optional:

                if dsu.find(u) == dsu.find(v):
                    continue

                if s >= x:
                    dsu.union(u, v)
                    used += 1

                elif s * 2 >= x and upgrades < k:
                    upgrades += 1
                    dsu.union(u, v)
                    used += 1

                if used == n - 1:
                    return True

            return used == n - 1

        left, right = 0, 2 * 10**5
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
