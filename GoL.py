import random
board_state = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
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
    for row in range(height):
        for col in range(width):
            board[row][col] = random.randint(0, 1)
    return board

def render(state):
    #dead cells = '%'; live cells = '#'
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
                print('%', " ", end="")
            else:
                print('#', " ", end="")
        print("|\n")

    print("|", end="")
    for col in range(cols*3):
        print("-", end="")
    print("|\n")

def count_neighbors(board, row, col):
    #if row == 0, then above = board[len(board) - 1][col-1] + board[len(board)-1][col] + board[len(board)-1][col+1]
    
    above =  board[row - 1][col - 1] + board[row - 1][col] + board[row - 1][col + 1]
    print("row above: " + str(board[row-1][col-1]) + " " + str(board[row - 1][col]) + " " + str(board[row - 1][col + 1]))
    print("above: " + str(above))
    
    adjacent = board[row][col - 1] + board[row][col + 1]
    print("current row: " + str(board[row][col-1] ) + " " + str(board[row][col]) + " " + str(board[row][col+1]))
    print("adjacent: " + str(adjacent))
    
    below = board[row + 1][col - 1] + board[row + 1][col] + board[row + 1][col + 1]
    print("row below: " + str(board[row+1][col-1]) + " " + str(board[row+1][col]) + " " + str(board[row+1][col+1])  )
    print("below: " + str(below))

    #TODO: add support for first/last rows/columns
    return above + adjacent + below
    
def next_board_state(board):
    live_neighbors = 0
    rows = len(board)
    columns = len(board[0])
    for row in range(rows):
        for col in range(columns):
            #if live cell has 0, 1 living neighbors, it dies
            if board[row][col] == alive:
                print("cell is alive!")
                count = count_neighbors(board, row, col) 
        
      
            #If a live cell has 2, 3 living neighbors, it stays alive
            #if a live cell has more than 3 living neighbors, it dies
            #If a dead cell has exactly 3 neighbors, it comes to life


#width = int(input("Enter size of width: "))
#height = int(input("Enter size of height: "))

width = 5
height = 5

board = random_state(width, height)

""" for i in range(height):
    for j in range(width):
        print("cell [" + str(i) + "]" + "[" + str(j) + "]" )
        print("living neighbors: " + str(count_neighbors(board, i, j))) """

count_neighbors(board, 2, 2)
#render(board)