import math

class Solution:
    def combine(self, n: int, k: int): #-> List[List[int]]:
        # times = self.choose(n, k)
        result = []
        for i in range(n):
            for j in range(n+1, 1, k):
                result.append([i+1, j+1])
            
        return(result)
    
    # def choose(self, n: int, k: int) -> int:
    #     return math.factorial(n) // math.factorial(k) // math.factorial(n-k)
    
num = Solution()
print(num.combine(5, 2))