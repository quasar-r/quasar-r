class Solution:
    def lengthOfLongestSubstring(s):
        counter = 0
        for i in range(len(s)):
            temp  = s[i]
            c = 1
            for j in range(i+1,len(s)):
                if s[j] not in temp:
                    c = c+1
                    temp+=s[j]
                else:
                    i = i+temp.index(s[j])+1
                    break
            if counter < len(temp):
                counter = len(temp)
        return counter

cou = Solution.lengthOfLongestSubstring("pwpwpkew")
print(cou)
