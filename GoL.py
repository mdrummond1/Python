import random
board_state = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

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
            if state[row][col] == 0:
                print('%', " ", end="")
            else:
                print('#', " ", end="")
        print("|\n")

    print("|", end="")
    for col in range(cols*3):
        print("-", end="")
    print("|\n")

width = 10
height = 2

board = random_state(width, height)

render(board)