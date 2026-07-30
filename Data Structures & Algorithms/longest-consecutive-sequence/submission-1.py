class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for i in nums:
            if i-1 not in numsSet:
                count = 1
                while i+1 in numsSet:
                    count+=1
                    i+=1
                res = max(res,count)

        return res
            
            