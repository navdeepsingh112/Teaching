n = int(input("ener n: "))
# for i in range(n):
#     if(i==0):
#         print(' ' * (n-1)  , '*' , sep='')
#     elif(i==n-1):
#         print('*' * (2*n-1))
#     else:
#         print(' ' * (n-i-1) ,'*' , ' ' * (2*i - 1) , '*',sep='')
#     # print()
for i in range(n):
    for j in range(2*n-1):
        if(i==0 and j==n-1):
               print('*',end='')
        elif(i==0):
             print(' ',end='')
        elif(i==n-1):
             print('*',end='')
        elif(j == n-i-1 or j==n+i-1):
             print('*',end='')
        else:
             print(' ',end='')
    print()
        
        