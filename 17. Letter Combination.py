class Solution:
    def letterCombinations(self, digits: str): #-> List[str]:
        result = []
        
        def backtrack(combination, nextDigits):
            if len(nextDigits) == 0:
                result.append(combination)
            else:
                digit = nextDigits[0]
                letters = phoneMapping[digit]
                for letter in letters:
                    backtrack(combination + letter, nextDigits[1:])
        
        phoneMapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv", 
            "9": "wxyz"
        }
            
        if not digits:
            return []
        
        backtrack("",digits)
        return result

# sol = Solution()
# print(sol.letterCombinations("34"))