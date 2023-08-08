# str = " This is Hello  World  "
# str = str.strip()
# print(str)
# split_str = str.split(" ")
# print(split_str)
# split_str.remove('')
# print(split_str)
# result = ""
# for itme in split_str:
#     result += itme + " "
# print(result)

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        split_str_list = []
        split_str_list = s.split(" ")
        result = ""
        for i in range(len(split_str_list)-1, -1, -1):
            if split_str_list[i] !=  '':
                result += split_str_list[i] + " "
        return result.strip()

in_str = "a good  example"
sol = Solution()
print(sol.reverseWords(in_str))      