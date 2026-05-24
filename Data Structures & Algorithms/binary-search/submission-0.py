class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # out = {}
        res = -1
        for i, n in enumerate(nums):
            if n == target:
                res = i
        return res


