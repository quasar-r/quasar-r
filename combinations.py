def combinations(lst):
    if lst:
      result = combinations(lst[:-1])
      return result + [c + [lst[-1]] for c in result]
    else:
      return [[]]
lst = ["a","b","c"]
combinations(lst)
