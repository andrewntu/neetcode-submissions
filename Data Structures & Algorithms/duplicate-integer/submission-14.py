class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        # target = 0
        # res = False
        for i, n in enumerate(nums):
            # diff = target - n
            if n in nums_dict:
                return True
            nums_dict[n] = i
        return False
        # res = False
        # nums.sort()
        # l, r = 0, len(nums) -1
        # while r > l:
        #     if nums[l] < nums[r]:
        #         r -= 1
        #     elif nums[l] == nums[r]:
        #         res =  True
        #     else:
        #         res = False
        # return res
            