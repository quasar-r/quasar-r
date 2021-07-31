class Solution:
    def longestPalindrome(s):
        length = 0
        st = 0
        ed = 0
        res = ''
        if s == "" or s == None:
            return st[st:ed]
        for i in range(len(s)):
            odd = expand_(s,i,i)
            even = expand_(s,i,i+1)
            temp = max(odd,even)
            if length < temp:
                st = i - int(round(temp-1)/2)
                ed = int(i+temp/2)+1
                length = temp
        return s[st:ed]
def expand_(st,le,re):
            while le>=0 and re<=len(st)-1:
                if st[le] != st[re]:
                    break
                le=le-1
                re+=1
            return re-le-1

print(Solution.longestPalindrome("cbb"))
