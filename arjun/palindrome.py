string = input("Enter String   : ")

n = len(string)

flag = True #haigaa palindrome

for i in range(0,n//2):

    if( string[i] != string[n-1-i]):

        flag = False
        break

if(flag):

    print("Palindrome")

else:

    print("Not pallindrome") 

   

