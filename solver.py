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

try_board = [
    [4,7,2,9,1,0,0,0,0],
    [0,0,8,0,5,0,0,9,1],
    [9,0,1,6,0,0,2,0,3],
    [0,0,0,4,7,0,5,0,0],
    [5,8,9,1,0,2,0,0,0],
    [7,4,0,0,3,8,9,0,2],
    [3,9,4,0,0,0,0,5,0],
    [8,0,0,0,0,0,6,2,0],
    [2,0,0,0,0,0,3,0,4]
]


def solve(board):
    """
    This function gets a board and attempts to solve it recursively.
    :param board: board 2d array
    :return: True if the board was solved, and False otherwise.
    """
    new_space = find_empty(board)

    if not new_space:
        # no empty spaces were found, sudoku is solved!
        print_board(board)
        print("Finished solving board!")
        return True

    row, col = new_space

    # Empty space was found
    for i in range(1, 10):
        # Check all the possible numbers, if valid found go with it
        if valid(board, i, (row, col)):
            # Edit the board and try again
            board[row][col] = i
            # Check for future solutions with new board
            if solve(board):
                return True
            # Failed to solve using the edit, reverse the change
            board[row][col] = 0

    return False


def valid(board, num, pos):
    """
    The function receive a board, a number to validate and the current position.
    It checks whether the given number fits the given position (that the number was not found in a
    row/col/adjacent positions already)
    :param board: board 2d array
    :param num: number to check for
    :param pos: position to place the number in
    :return: True or False depending if the number is valid in the given position.
    """

    # check col
    for i in range(len(board)):
        if pos[0] != i and board[i][pos[1]] == num:
            return False

    # check row
    for i in range(len(board[0])):
        if pos[1] != i and board[pos[0]][i] == num:
            return False

    # calc square x start
    start_x = pos[1] // 3 * 3

    # calc square y start
    start_y = pos[0] // 3 * 3

    # Go over y axis
    for i in range(start_y, start_y + 3):
        # Go over x axis
        for j in range(start_x, start_x + 3):
            # Check that the current position is not checked
            if i != pos[0] or j != pos[1]:
                if board[i][j] == num:
                    return False

    return True


def print_board(board):
    """
    Displays the board to the console
    :param board: board 2d array
    :return:
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- " * 12)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """
    Finds first empty spot in the board, if one exists
    :param board: board 2d array
    :return: if empty spot found, return its' coordinates, otherwise return None.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col

    return None


def check_board(board):
    """
    Helper function that gets a board and checks its' validity
    :param board: board 2d array
    :return: True or False depending if the board is valid.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                if not valid(board, board[i][j], (i, j)):
                    return False

    return True


if __name__ == '__main__':
    check_board(board)

    # Attempt to solve board:
    solve(board)