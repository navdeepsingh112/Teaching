

# *
# **
# ***
# ****


for i in range(0,5):

    for j in range(0,5):

        if (j>i and j<2+i) or (j>=i and j>= 2+i) :

         print("*" , end=" ")

        else:

         print(" " , end=" ")
    

    print()





