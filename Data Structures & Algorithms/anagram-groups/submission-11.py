class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            key = ''.join(sorted(i))
        
            if key not in res:
                res[key] = []
            res[key].append(i)
        return list(res.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         str_save = {}

        # for word in strs:
        #     key = ''.join(sorted(word))
        #     if key not in str_save:
        #         str_save[key] = []
        #     str_save[key].append(word)

#         return list(str_save.values())