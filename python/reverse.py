s = "abcdef"
n = len(s)
print(s[0:3])
print(s[0:7:2])
print(s[5:2:-1])
# [start : end : gap] works like range
# for i in range(n):
#     print(s[i]) #accessing it from the front
#     print(s[n-1-i]) # accessing it from the back
# for i in range(-1 , -n-1 , -1):
#     print(s[i])

# n =3
# abc
# -1 -2 -3
#indexing
# a  b  c  d  e  f
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1
# start - end
# 0 - n-1
# -n - -1