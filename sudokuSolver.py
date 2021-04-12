board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#--------------------------------------------------------------------------------------------
#this function prints the board.
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") #this is for proper spacing

#print_board(board)
#--------------------------------------------------------------------------------------------
def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col]==0:     #if row,col == 0, return that location.
                return (row,col)    #row,col because solver goes from left to right.

    return None     #if no blank squares remaine, return none.
#--------------------------------------------------------------------------------------------    
def valid(bo,num,pos):
    #checking row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] !=i: #this is to make sure you dont check against the number you just put in
            return False
    #check column
    for i in range (len(bo)):
        if bo[i][pos[1]] == num and pos[0] !=i: #this is to make sure you dont check against the number you just put in
            return False

    #check 3x3 box
    box_x = pos[1] //3  #posible positions are from 0-2. (0,0), (0,1), (0,2), (1,0), etc...
    box_y = pos[0] //3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True     #if it passes all the checks above, then it is a valid position, return true.
#--------------------------------------------------------------------------------------------
def solve(bo):  #solving the board using recursion
    find = find_empty(bo)
    if not find:    #meaning there are no more emptry spaces in the board.
        return True #you are done, the board is filled out. This is the base case in the recursion
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(bo, i, (row,col)):     #go through the board to check if the number input is valid
            bo[row][col] =i             #if it is valid, insert the number in board.

            if solve(bo):               #use recursion to fill the board out and make sure the number works.
                return True

            bo[row][col] = 0            #if recursion is ended (the number input doesn't work), then set the number to zero and try again.
    return False                       
#--------------------------------------------------------------------------------------------
print_board(board)
solve(board)
print("___________________")
print_board(board)