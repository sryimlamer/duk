import copy
print("Welcome to the game! ")


def beginning_of_the_game():
    """Getting the dimension of the game field"""

    size = input("Please, input the number of the cell: ")
    while type(size) != int:
        try:
            size = int(size)
        except ValueError:
            print("Input error. No number was entered.")
            size = input("Please, input the number of the cell: ")
        else:
            pass
    else:
        return size


def dimension_of_the_map(size):
    """The creation of the field of play"""
    height = ['.' for _ in range(size)]
    dimension = []
    for _ in range(size):
        dimension.append(height.copy())
    return dimension
    

def checking_win_lose(board1, board2, k):
    """Method for checking win-loss"""
    count_first = 1
    """check horizontal for p1"""
    for i, x in enumerate(board1):
        for j, y in enumerate(board1[i][:-1]):
            if board1[i][j] == 'X' and board1[i][j + 1] == 'X':
                count_first += 1
                if count_first == k:
                    return 1, "Player 1 win. The end."
    """check vertical for p1"""
    count_first = 1
    for i, x in enumerate(board1[:-1]):
        for j, y in enumerate(board1[i]):
            if board1[i][j] == 'X' and board1[i+1][j] == 'X':
                count_first += 1
                if count_first == k:
                    return 1, "Player 1 win. The end."
    """check horizontal for p2"""
    count_second = 1
    for i, x in enumerate(board2):
        for j, y in enumerate(board2[i][:-1]):
            if board2[i][j] == 'O' and board2[i][j + 1] == 'O':
                count_second += 1
                if count_second == k:
                    return 2, "Player 2 win. The end."
                    
    """check vertical for p2"""
    count_second = 1
    for i, x in enumerate(board2[:-1]):
        for j, y in enumerate(board2[i]):
            if board2[i][j] == 'O' and board2[i+1][j] == 'O':
                count_second += 1
                if count_second == k:
                    return 2, "Player 2 win. The end."
    return None, ""


"""Checking the number in coordinates"""


def checking_coor(in_coor):
    while type(in_coor) != int:
        try:
            in_coor = int(in_coor)
        except ValueError:
            print("Input error. No number was entered.")
            in_coor = input("Please, input the number of the cell: ")
        else:
            pass
    else:
        promo = in_coor
        return promo


"""The x coordinate is the row selection. The y-coordinate is the column selection"""


def get_coor1x():
    player_1_x = input("Coordinate of X: ")
    player_1_x = checking_coor(player_1_x)

    x_coordinate_1 = player_1_x - 1
    return x_coordinate_1


def get_coor1y():
    player_1_y = input("Coordinate of Y: ")
    player_1_y = checking_coor(player_1_y)

    y_coordinate_1 = player_1_y - 1
    return y_coordinate_1


def get_coor2x():
    player_2_x = input("Coordinate of X: ")
    player_2_x = checking_coor(player_2_x)

    x_coordinate_2 = player_2_x - 1
    return x_coordinate_2


def get_coor2y():
    player_2_y = input("Coordinate of Y: ")
    player_2_y = checking_coor(player_2_y)

    y_coordinate_2 = player_2_y - 1
    return y_coordinate_2


def check_coor2(func):
    try:
        func
    except IndexError:
        check_coor2(func)
    else:
        return func


"""Getting the dimensions of the field"""


width = beginning_of_the_game()


k = input("Enter the number in a row required to win: ")


"""Getting the selected game mode"""
while type(k) != int:
    try:
        k = int(k)
    except ValueError:
        print("Input error. No number was entered.")
        k = input("Please, input the number of the cell: ")
    else:
        pass


game_mode = 1


"""Getting the created field"""
dim = dimension_of_the_map(width)

print('Your map is ready! ')
for i in range(width):
    print(dim[i])

"""Creating separate arrays with noughts and crosses"""
player_1_board = copy.deepcopy(dim)
player_2_board = copy.deepcopy(dim)

print("If you want to do a step. Enter x and then y.")

player = 1
"""Man vs man game mode"""
while game_mode == 1:

    if player == 1:
        print("First player's turn. X")

        x_coordinate_1 = get_coor1x()
        y_coordinate_1 = get_coor1y()

        while dim[y_coordinate_1][x_coordinate_1] == 'O':
            print('Step is impossible!')

            x_coordinate_1 = get_coor1x()
            y_coordinate_1 = get_coor1y()

        dim[y_coordinate_1][x_coordinate_1] = 'X'
        player_1_board[y_coordinate_1][x_coordinate_1] = 'X'
        winner, msg = checking_win_lose(player_1_board, player_2_board, k)

        if winner:
            print(msg)
            break

        for i in range(width):
            print(dim[i])

        player = 2
    if player == 2:

        print("Second player's turn. O")

        x_coordinate_2 = get_coor2x()
        y_coordinate_2 = get_coor2y()

        while dim[y_coordinate_2][x_coordinate_2] == 'X':
            print('Step is impossible!')

            x_coordinate_2 = get_coor2x()
            y_coordinate_2 = get_coor2y()

        dim[y_coordinate_2][x_coordinate_2] = 'O'
        player_2_board[y_coordinate_2][x_coordinate_2] = 'O'
        winner, msg = checking_win_lose(player_1_board, player_2_board, k)
        if winner:
            print(msg)
            break

        for i in range(width):
            print(dim[i])
        player = 1
