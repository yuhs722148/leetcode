class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = [candy+extraCandies >= max_candy for candy in candies]
        return result
    
# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         result = []
#         max_candy = max(candies)
#         for candy in candies:
#             if candy + extraCandies < max_candy:
#                 result.append(False)
#             else:
#                 result.append(True)
#         return result