class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            hashtable[i] = 1
        # [0=>1,1=>1,2=>1,3=>1]
        for i in range(len(nums)):
            for j in dict.keys(hashtable):
                if j!=i:
                    hashtable[j] = hashtable[j] * nums[i]
        return list(dict.values(hashtable))