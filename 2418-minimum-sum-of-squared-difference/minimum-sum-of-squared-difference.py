class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        d = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        if sum(d) <= k:
            return 0

        n = len(d)
        d.append(0)  # sentinel
        for i in range(n):
            cnt = i + 1
            cost = cnt * (d[i] - d[i + 1])
            if k >= cost:
                k -= cost
            else:
                level = d[i] - k // cnt      # common level of the top cnt elements
                extra = k % cnt              # these get one more reduction
                tail = sum(x * x for x in d[cnt:n])
                return tail + extra * (level - 1) ** 2 + (cnt - extra) * level ** 2