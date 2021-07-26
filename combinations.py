def combinations(lst):
    if lst:
      result = combinations(lst[:-1])
      return result + [c + [lst[-1]] for c in result]
    else:
      return [[]]
lst = ["a","b","c"]
combinations(lst)

'''
n = ["a","b","c"]

def comb(n):
    if len(n) == 0:
        return [[]]
    res= []
    char = n[0]
    coms = comb(n[1:])
    interal_ = []
    for each in coms:
        interal_.append(each+[char])
    res.extend(interal_+coms)
    return interal_+coms
x = comb(n)
print(x)
'''
