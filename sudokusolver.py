## sudoku solver with back tracking agorithm

board = [
    [7,8,0,4,7,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,2,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]

  ]



def display_board(bod):

    for i in range(len(bod)):  #gets the range of the whole board in rows()
        if i % 3 == 0 and i != 0:
            print("--------------------")

        for j in range(len(bod[0])): # gets the range of board in columns
            if j %3 == 0 and j != 0 :
                print("|" , end=""  )

            if j == 8:
                print(bod[i][j])

            else:
                print(str(bod[i][j]) + " ", end ="")


#display_board(board)

def empty_space(bod):
    for i in range(len(bod)):
        for j in range(len(bod[0])):

            if bod[i][j] == 0:
                return (i ,j) #row column

    return None


def valid(bod, num, pos):

    #check row
    for i in range(len(bod[0])):
        if bod[pos[0]][i] == num and pos[1] != i:
            return False
        # checks each element in the row and check if it is equal to whatever num you just added in

    #check columns
    for i in range(len(bod)):
        if bod[i][pos[1]] == num and pos[0] != i:
            return False
        #check ech element in the column and check if it is equal to whatever num you just added
        
    #check box(3x3 cube)
    boxX= pos[1] // 3
    boxY= pos[0] // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            #checing if any other element is equal to the one we just added and not check the current position we just inputed
            if bod[i][j] == num and (i,j) != pos:
                return False

    return True



def final(bod):
    #writing up the algorithm that uses the functions and backtracks for us
    find = empty_space(bod)
    if not find:
        return True #solution has been found and the board is done
    else:
        row, col = find

    for i in range(1,10):
        if valid(bod, i, (row, col)):     #(Checking if added i is a valid soultion )
            bod[row][col] = i

            if final(bod):
                return True

            bod[row][col] = 0  #if new position is not valid .reset it to 0 bc it cant be correc
    return False





    #return False

display_board(board)
final(board)
print("-------------")
display_board(board)
#print("+++++++++++++++++++")
final((board))

