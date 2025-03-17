

# *
# **
# ***
# ****


for i in range(1,5):

    for j in range(1,5):

        if (j>i and j<2+i) or (j>=i and j>= 2+i) :

         print("*" , end=" ")

        else:

         print(" " , end=" ")
    

    print()





