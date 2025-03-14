# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# My Answer
def filter_list(l):
    i=0
    while len(l)>i:
        if isinstance(l[i],str):
            l.pop(i)
        else:
            i+=1
            
    return l

# Best Answer

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
  
