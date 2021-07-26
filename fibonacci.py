n = 7
arr = [0,1] 
#[0,1,1,2]
def fib(n):
    if n<=len(arr):
        return arr[n-1]
    
    sum_ =  fib(n-1)+fib(n-2)
    arr.append(sum_)
    return sum_
x = fib(n)
print(x)
print(arr)
