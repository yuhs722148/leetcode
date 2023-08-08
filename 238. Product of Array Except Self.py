class Solution:
    def productExceptSelf(self, nums):#: List[int]):# -> List[int]:
        result = []
        
        for i in range(len(nums)):
            temp = 1
            
            for j in range(len(nums)):
                if j != i:
                    temp *= nums[j]
                    
            result.append(temp)
            
        return result
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4,5,6,6,6]))
            