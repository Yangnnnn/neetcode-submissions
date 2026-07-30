class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for i in nums:
            count = 0 
            while i-1 in numsSet:
                i=i-1
                count+=1
            res = max(res,count+1)
        return res
            
            