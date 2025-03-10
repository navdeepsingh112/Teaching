string = input("enter string : ")
n = len(string)
# f= True
# for i in range(0 , n//2): # double // is integer divison ans is int
#     if( string[i] != string[-1-i]): #accessing string from front and reverse at the same time
#         f=False
#         break
# if(f):
#     print("palindrome")
# else:
#     print("not palindrome")
# print(string[0:(n//2 )+1])
# print(string[n-1:(n-1-n//2):-1])

if(string[0:(n//2 )] == string[n-1:(n-1-n//2):-1]):
    print("palindrome")
else:
    print("not a palindrome")