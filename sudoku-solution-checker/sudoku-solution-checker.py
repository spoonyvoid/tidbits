#TO-DO: Use numpy instead of the current threebythree_board solution

#A 9x9 Sudoku solution checker

def display_board(board):
    """
    Displays the 9x9 Sudoku board in a nicer way
    """
    print("\nThis is your Sudoku solution:")
    for row in board:
        print("\n|", end = "")
        for element in row:
            print(f" {element} |", end = "")
    print("\n")

def board_validator(board):
    """
    Checks to see if every sub-list in a nested list (or every horizontal
    row on a board) is comprised of the digits 1 to 9 (inclusive) with
    no repetitions.
    """
    expected = [1,2,3,4,5,6,7,8,9]
    for row in board:
        if sorted(row) == expected:
            continue
        else:
            return False
    return True

def sudoku_checker(board):
    """
    Checks to see if a 9x9 Sudoku solution in the form of nested lists
    is right. This includes ensuring that every row, every column and every
    3x3 square on the board contains the digits 1 to 9 (inclusive) with
    no repetitions.
    """
    #Checking each horizontal row on the board
    horizontal_status = board_validator(board)

    #Checking each vertical column on the board by transposing the board first
    transposed_board = list(map(list, zip(*board)))
    vertical_status = board_validator(transposed_board)

    #Checking each 3 by 3 square on the board
    threebythree_board = []

    #What the following essentially does is pop the first three items
    #in the first three rows (sub-lists) to store them in a holder list
    #called "block_list". Once the length of block_list is 9 (or in other words
    #we have popped a 3x3 block), we store that in our threebythree_board list,
    #keep track of the number of blocks we've popped so far, and empty the
    #block_list to store the next 3x3 block. Once we reach the last row (that
    #is last of the 3 left-most blocks), we reset the row variable to 0 so we
    #can begin popping the next 3 blocks. The iteration ends when we've
    #popped 9 blocks (or blocks = 8).

    row = 0
    blocks = 0
    block_list = []

    while row < 9 and blocks < 9:
        #Popping the first 3 items from a row
        t = 0
        while t < 3:
            block_list.append(board[row].pop(0))
            t += 1

        #If we've got a block, we add that to the main threebythree_board
        #list and empty the block_list and keep track of the number of
        #blocks we've popped so far
        if len(block_list) == 9:
            threebythree_board.append(block_list)
            blocks += 1
            block_list = []

        #If we've reached the last row (as long as we haven't popped all
        #the blocks) then we reset the row count to 0. If not we move on to
        #the next row.
        if row == 8 and blocks < 9:
            row = 0
        else:
            row += 1

    threebythree_status = board_validator(threebythree_board)

    #Determining if the all 3 conditions have been met or in other words
    #if the solution for this Sudoku puzzle is accurate
    if vertical_status and horizontal_status and threebythree_status:
        return "Well done! You've solved it!"
    else:
        return "Nope, you haven't solved it. Try again!"

print("""Enter in your Sudoku solution line by line. Please make sure to use
only integers and please insert a comma after every integer. Do not insert
a space after the comma!
E.g. 4,5,6,1,2,3,7,8,9""")

line_no = 1
user_board = []

while line_no <= 9:
    try:
        row = input(f"\nEnter Line {line_no} Now\n> ").split(',')

        #Data validation to prevent empty spaces, illegal characters,
        #non-integers, non-positive integers, and lists that aren't 9
        #elements in length.
        for item in row:
            if item == "" or item == " ":
                print("You've entered an empty space or an extra comma!")
                raise ValueError
            elif item.isdigit() == False:
                print("You've entered a non-integer!")
                raise ValueError
            elif int(item) > 9 or int(item) == 0:
                print("You cannot have 0 or numbers greater than 9!")
                raise ValueError

        if len(row) != 9:
            print("You didn't enter in 9 integers or missed a comma!")
            raise ValueError

        user_board.append(list(map(int, row)))
        line_no += 1

    except ValueError:
        print("Please Try Again!")
        continue

display_board(user_board)
print(sudoku_checker(user_board))

#Tests
#print(sudoku_checker([[1, 3, 2, 5, 7, 9, 4, 6, 8],
#[4, 9, 8, 2, 6, 1, 3, 7, 5],
#[7, 5, 6, 3, 8, 4, 2, 1, 9],
#[6, 4, 3, 1, 5, 8, 7, 9, 2],
#[5, 2, 1, 7, 9, 3, 8, 4, 6],
#[9, 8, 7, 4, 2, 6, 5, 3, 1],
#[2, 1, 4, 9, 3, 5, 6, 8, 7],
#[3, 6, 5, 8, 1, 7, 9, 2, 4],
#[8, 7, 9, 6, 4, 2, 1, 5, 3]]) == "Solved!")

#print(sudoku_checker([[1, 3, 2, 5, 7, 9, 4, 6, 8],
#[4, 9, 8, 2, 6, 1, 3, 7, 5],
#[7, 5, 6, 3, 8, 4, 2, 1, 9],
#[6, 4, 3, 1, 5, 8, 7, 9, 2],
#[5, 2, 1, 7, 9, 3, 8, 4, 6],
#[9, 8, 7, 4, 2, 6, 5, 3, 1],
#[2, 1, 4, 9, 3, 5, 6, 8, 7],
#[3, 6, 5, 8, 1, 7, 9, 2, 4],
#[8, 7, 9, 6, 4, 2, 1, 3, 5]]) == "Try Again!")
