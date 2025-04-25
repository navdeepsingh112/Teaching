# fruits = ['apple' , 'orange', 'guava']
# upper_fruits = list(map(str.upper , fruits))
# print(upper_fruits)
from functools import reduce

L = [1,2,3,4]
newL = list(map(range , L))
print(newL)
for i in newL:
    print(list(i))
#apply a function to each element of the list
#
def summ(n1 , n2 ):
    return n1+n2
nos = [1,2,3,4,5,6]
result = reduce(summ , nos)
print(result)
#reduces the list to a single object
#new add
