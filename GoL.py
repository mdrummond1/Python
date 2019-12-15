import random
board_state = [
    [0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 0]
]

alive = 1
dead = 0

def dead_state(width, height):
    #build a board that is size width x height
    board = []
    for col in range(width):
        board.append(0)
    state = [board]

    for row in range(height - 1):
        state.append(board)

    return state

def random_state(width, height):
    #build board with dead_state
    board = dead_state(width, height)

    #randomize board
    print("before randomizing: " + str(board)) 

    for row in range(height):

        for col in range(width):
            print("board[" + str(row) + "][" + str(col) + "] before: " + str(board[row][col]))
            board[row][col] = random.randint(0, 1)
            """ if random.random() > 0.5:
                board[row][col] = 1
            else:
                board[row][col] = 0 """
        print("board[" + str(row) + "] after: " + str(board[row]))


    
    print("board after randomizing: " + str(board))
    return board

def render(state):
    #dead cells = '.'; live cells = '#'
    rows = len(state)
    cols = len(state[0])
    print("|", end="")
    for col in range(cols*3):
        print("-", end="")
    print("|\n")
    
    for row in range(rows):
        print("|", end="")
        for col in range(cols):
        #print rows
            cell = state[row][col]
            if cell == 0:
                print('.', "", end="")
            else:
                print('#', "", end="")
        print("|\n")

    print("|", end="")
    for col in range(cols*3):
        print("-", end="")
    print("|\n")

def count_neighbors(board, row, col):
    #if row == 0, then above = board[len(board) - 1][col-1] + board[len(board)-1][col] + board[len(board)-1][col+1]
    """
    cases:
        1. first row and first column
        2. first row and a middle column
        3. first row and last column
        4. a middle row and first column
        5. a middle row and a middle column
        6. middle row and last column
        7. last row and first column
        8. last row and a middle column
        9. last row and last column
    """    
    prev_row = row - 1 
    next_row = row + 1
    prev_col = col - 1
    next_col = col + 1

    """ print("# of columns: " + str(len(board[0])))
    print("# of rows: " + str(len(board)))
    print("passed in row " + str(row) + " and column " + str(col)) """


    #if first row, previous row is the last row
    if row == 0:
        prev_row = (len(board) - 1)
        #print("prev_row set to " + str(prev_row))

    
    #if last row, next row is the first row
    elif row == (len(board) - 1):
        next_row = 0
       # print("next_row set to " + str(next_row))
    
    #if first column, previous column is the last column
    if col == 0:
        prev_col = len(board[0]) - 1
      #  print("prev_col set to " + str(prev_col))
    
    
    #if last column, next column is the first column
    elif col == (len(board[0]) - 1):
        next_col = 0
     #   print("next_col set to " + str(next_col))
    
    #print("prev_row: " + str(prev_row))
    #print("row: " + str(row))
    #print("next_row: " + str(next_row))
    #print("prev_col: " + str(prev_col))
    #print("col: " + str(col))
    #print("next_col: " + str(next_col))
    
    #                1           3               1       4               1           5
    above = board[prev_row][prev_col] + board[prev_row][col] + board[prev_row][next_col]
    #print("row above: " + str(board[prev_row][prev_col]) + " " + str(board[prev_row][col]) + " " + str(board[prev_row][next_col]))
    #print("above: " + str(above))
    
    adjacent = board[row][prev_col] + board[row][next_col]
    #print("current row: " + str(board[row][prev_col]) + " " + str(board[row][col]) + " " + str(board[row][next_col]))
    #print("adjacent: " + str(adjacent))
    
    below = board[next_row][prev_col] + board[next_row][col] + board[next_row][next_col]
    #print("row below: " + str(board[next_row][prev_col]) + " " + str(board[next_row][col]) + " " + str(board[next_row][next_col])  )
    #print("below: " + str(below))

    #TODO: add support for first/last rows/columns
    return above + adjacent + below
    
def next_board_state(initial_state):

    next_state = dead_state(len(initial_state[0]), len(initial_state))

    rows = len(initial_state)
    columns = len(initial_state[0])
    for row in range(rows):
        for col in range(columns):
            if initial_state[row][col] == 1:
                #print("cell is alive!")
                count = count_neighbors(initial_state, row, col)
            
                #if a live cell has more than 3 living neighbors, it dies
                if count > 3:
                    #print("the cell died")
                    next_state[row][col] = 0
                
                #If a live cell has 2, 3 living neighbors, it stays alive
                elif count > 1:
                    #print("the cell stays alive!")
                    next_state[row][col] = 1

                #if live cell has 0, 1 living neighbors, it dies
                elif count >= 0:
                    #print("the cell died!")
                    next_state[row][col] = 0
                
                #otherwise keep the same state
                else:
                    next_state[row][col] = initial_state[row][col]
                
            
            #If a dead cell has exactly 3 neighbors, it comes to life
            else:
                next_state[row][col] = 1
    return next_state

#width = int(input("Enter size of width: "))
#height = int(input("Enter size of height: "))
#print(board_state)
#next_board_state(board_state)



"""
board
1   1   1   1   1   1   1
1   1   1   1   1   1   1
1   1   1   1   1   1   1
1   0   1   1   1   1   1
1   1   1   1   1   1   1


print("case 1: ")
count_neighbors(board, 0, 0)

print("case 2: ")
count_neighbors(board, 0, 2)

print("case 3: ")
count_neighbors(board, 0, 4)

print("case 4: ")
count_neighbors(board, 3, 0)

print("case 5: ")
count_neighbors(board, 2, 3)

print("case 6: ")
count_neighbors(board, 3, 4)

print("case 7: ")
count_neighbors(board, 4, 0)

print("case 8: ")
count_neighbors(board, 4, 2)

print("case 9: ")
count_neighbors(board, 4, 4)"""
def main():
    width = 7
    height = 5    
    random_state(width, height)
    #board = board_state
    #render(board)
    
    #board = next_board_state(board)
    #render(board)
if __name__ == "__main__":
    main()


