class Rec:
    def find_perm(self, str_s):
        return self.perm_str(str_s)
    def perm_str(self,str_s):
        if len(str_s) == 1:
            return [str_s[-1]]
        char = str_s[0]
        set_ = self.perm_str(str_s[1:])
        result = []
        for each in set_:
            for i in range(0,len(each)+1):
                result.append(each[:i]+char+each[i:])
        return result
str_s = "abc"
re = Rec()
all_perms = re.find_perm(str_s)
print(all_perms)
    
