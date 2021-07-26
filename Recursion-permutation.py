class Rec:
    
    def __init__(self):
        self.res = []
    def find_perm(self, nums):
        self.perm(nums,[])
        return self.res
    def perm(self,nums,path):
        if len(nums) == 0:
            return self.res.append(path)
        for i in range(0,len(nums)):
            x = nums.pop(i)
            self.perm(nums,path+[x])
            '''
            if nums is  string
            nums = "abc"
            for loop will only have below code as string are immutable so we can slice and pass substring without poping or inserting
            perm_str(s[:i]+s[i+1:],path+s[i])
            '''
            nums.insert(i,x)

nums=[1,2,3]
#nums = "abc"
obj = Rec()
result = obj.find_perm(nums)
print(result)
