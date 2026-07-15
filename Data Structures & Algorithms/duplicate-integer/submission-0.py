class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for i in nums:
            if i in hashtable:
                return True
            else:
                hashtable[i] = 1
        return False