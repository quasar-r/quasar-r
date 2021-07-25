class Rec:
    
    def __init__(self):
        self.res = []
        
    def find_perm(self, nums):
        self.perm(nums,[])
        return self.res
        

    def perm(self,nums,path):
        if len(nums) == 0:
            return self.res.append(path)
            '''
            in case of string 
            return self.res.append("".join(path))
            '''
        for i in range(0,len(nums)):
            print(nums[i])
            x = nums.pop(i)
            self.perm(nums,path+[x])
            nums.insert(i,x)

nums=[1,2,3]
'''
if nums is array of string
nums = ["a","b","c"]
if nums is string of alphabet
nums="abc"
nums = list(nums)
'''
obj = Rec()
result = obj.find_perm(nums)
print(result)
