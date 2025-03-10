def print_board(user_input):
    for i in range (3):
        for j in range(3):
            print(" ",user_input[i][j],' |' if j!=2 else "",end="",sep="")
        print()
        if(i!=2):
            print("---+"*2,'---',sep='')
def not_win(user_input):
    for i in range(3):
        if((user_input[i][0]==user_input[i][1]==user_input[i][2]) and user_input[i][0] != ' ' ):
            print(user_input[i][0],'Won')
            return False
    for j in range(3):
        if((user_input[0][j]==user_input[1][j]==user_input[2][j]) and user_input[0][j] != ' '):
            print(user_input[0][j],'Won')
            return False
    if((user_input[0][0] == user_input[1][1] == user_input[2][2]) and user_input[0][0] != ' '):
        print(user_input[0][0],'Wonnn')
        return False
    if((user_input[0][2] == user_input[1][1] == user_input[2][0]) and user_input[0][2] != ' '):
        print(user_input[1][1],'Wonn')
        return False
    f = False
    for i in range(3):
        for j in range (3):
            if(user_input[i][j] == ' '):
                f = True
                break
    if(f==False):
        print("no one won")
    return f
user_inp = [[' ',' ',' ',],
            [' ',' ',' ',],
            [' ',' ',' ',]]

print_board(user_inp)
turn =0
while(not_win(user_inp)):
    a = input("enter row")
    b = input("enter column")
    if(turn % 2 ==0):
        user_inp[int(a)-1][int(b)-1]='X'
    else:
        user_inp[int(a)-1][int(b)-1]='O'
    turn = turn +1
    print_board(user_inp)
# {work to do u if if is succesful} if {condition} else {work to do is if is not succesful}
#['0' , ' ' , ' '] at i =0.
#l=  [a,b,c,d]. l[i] # i = 0,1,2,3. l[0] = a , l[1] = b; l=[[a,b],[c,d]] i= 0,1, j = 0,1; i=0,j=0 a ;i=0,j=1 b;i=1,j=0 c;i=1,j=1 d