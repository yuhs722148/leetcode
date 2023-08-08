class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        result = ""
        for i in range(min_length):
            result += word1[i] + word2[i]
        result += word1[min_length:]
        result += word2[min_length:]
        return result
            
sol = Solution()
print(sol.mergeAlternately("abc","def"))