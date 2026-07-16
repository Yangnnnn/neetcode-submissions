class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        #[1,1,1,1]
        for i in range(len(result)):
            if i > 0:
                result[i] = result[i-1] *nums[i-1]

        #[1,x,x,x]
        #[1,1,x,x]
        #[1,1,2,x]
        #[1,1,2,8]
        right = 1
        for i in range(len(result)-1,-1,-1):
            result[i] = result[i] * right
            right = right*nums[i]
        return result

            
