# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        n = len(nums)

        for i in range(n):
            st = 0 - nums[i]
            hs = set()
            for j in range(i+1, n):
                comp = st - nums[j]

                if comp in hs:
                    tempList = tuple(sorted([nums[i], nums[j], comp]))
                    res.add(tempList)

                hs.add(nums[j])

        return [list(t) for t in res]