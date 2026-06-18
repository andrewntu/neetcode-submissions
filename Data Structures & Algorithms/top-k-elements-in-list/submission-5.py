class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        savenum = {}
        countnum = [[] for _ in range(len(nums) + 1)]
        # find the most, find second most, find next
        for i, n in enumerate(nums):
            if n in savenum:
                savenum[n] += 1
            else:
                savenum[n] = 1
        for i, n in savenum.items():
            countnum[n].append(i)
        res = []
        for x in range(len(countnum) -1 ,-1, -1):
            for num in countnum[x]:
                res.append(num)  # Append the actual number, not the list!
                
                # Check if we've gathered enough numbers yet
                if len(res) == k:
                    return res
        
        

        