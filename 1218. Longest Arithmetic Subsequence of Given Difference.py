def longestSubsequence(arr: list[int], difference: int) -> int:
    result = 0
    dp = {}
    for num in arr:
        if num - difference in dp:
            # 如果有其他值-差值的子序列已存在 長度+1
            dp[num] = dp[num - difference] + 1
        else:
            dp[num] = 1
        result = max(dp[num], result)
    return result

# def findSubsequence(arr: list[int], difference: int, index: int) -> int:
#     length = 1
#     print('index = ', index)
#     for i in range(index, len(arr)-1, 1):
#         print('arr[i+1] = ', arr[i+1], 'arr[i] = ', arr[i])
#         if(difference == (arr[i+1] - arr[i])):
#             length += 1
#         else:
#             break
#     print('length = ', length)
#     return length
        
# dp = {}
#     result = 0
#     for num in arr:
#         if num - difference in dp:
#             dp[num] = dp[num - difference] + 1
#         else:
#             dp[num] = 1
#         result = max(result, dp[num])
#     return result   

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(longestSubsequence(arr, difference))