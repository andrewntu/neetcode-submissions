class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_num = {}
        # nums.sort
        for i, n in enumerate(nums):
            diff = target - n
            if diff in need_num:
                return [need_num[diff],i]
            need_num[n] = i
