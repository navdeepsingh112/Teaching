def print_board(user_input):
    # Loop through the rows of the board
    for i in range(3):
        # Loop through the columns of the board
        for j in range(3):
            # Print each cell with a vertical separator unless it's the last column
            print(" ", user_input[i][j], ' |' if j != 2 else "", end="", sep="")
        print()  # Move to the next line after each row
        # Print horizontal separator after each row except the last one
        if i != 2:
            print("---+" * 2, '---', sep='')

def not_win(user_input):
    # Check for horizontal wins
    for i in range(3):
        if (user_input[i][0] == user_input[i][1] == user_input[i][2]) and user_input[i][0] != ' ':
            print(user_input[i][0], 'Won')
            return False
    # Check for vertical wins
    for j in range(3):
        if (user_input[0][j] == user_input[1][j] == user_input[2][j]) and user_input[0][j] != ' ':
            print(user_input[0][j], 'Won')
            return False
    # Check for diagonal wins (top-left to bottom-right)
    if (user_input[0][0] == user_input[1][1] == user_input[2][2]) and user_input[0][0] != ' ':
        print(user_input[0][0], 'Wonnn')
        return False
    # Check for diagonal wins (top-right to bottom-left)
    if (user_input[0][2] == user_input[1][1] == user_input[2][0]) and user_input[0][2] != ' ':
        print(user_input[1][1], 'Wonn')
        return False
    # Check if the board is full without a winner
    f = False
    for i in range(3):
        for j in range(3):
            if user_input[i][j] == ' ':  # If there is an empty cell, game continues
                f = True
                break
    if not f:
        print("no one won")
    return f

# Initialize an empty 3x3 tic-tac-toe board
user_inp = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

# Print the initial empty board
print_board(user_inp)

# Turn counter to alternate between 'X' and 'O'
turn = 0

# Main game loop - continues until there is a winner or a draw
while not_win(user_inp):
    # Get user input for row and column
    a = input("enter row")
    b = input("enter column")
    # Place 'X' or 'O' based on whose turn it is
    if turn % 2 == 0:
        user_inp[int(a)-1][int(b)-1] = 'X'
    else:
        user_inp[int(a)-1][int(b)-1] = 'O'
    # Increment turn counter
    turn += 1
    # Print the updated board
    print_board(user_inp)
# {work to do u if if is succesful} if {condition} else {work to do is if is not succesful}
#['0' , ' ' , ' '] at i =0.
#l=  [a,b,c,d]. l[i] # i = 0,1,2,3. l[0] = a , l[1] = b; l=[[a,b],[c,d]] i= 0,1, j = 0,1; i=0,j=0 a ;i=0,j=1 b;i=1,j=0 c;i=1,j=1 d