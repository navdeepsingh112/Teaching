def name(no1 , no2):
    print(no1-no2)
    if(no1== 11):
        return 0
    name(no1+2,no2+1)
    return no1+no2
print(name(1 ,2))

#recurssion : calling same function inside a function