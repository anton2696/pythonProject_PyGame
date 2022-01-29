import random


def init_board():
    # генирирует 2 цифры 2 цифры
    board = []
    for i in range(4):
        board += [["0"] * 4]
    addNewNum(board, 2)
    return board


def addNewNum(board, n):
    """Генерирует 2 или 4 и устанавливает число в случайном месте на доске,
   которое изначально равно 0.
       """
    for i in range(n):
        newNum = str(random.choice([2, 4]))
        randomx = random.randrange(4)
        randomy = random.randrange(4)
        while board[randomy][randomx] != "0":
            randomx = random.randrange(4)
            randomy = random.randrange(4)
        board[randomy][randomx] = newNum


def checkWin(board):
    """ Проверяет, есть ли у игрока номер 2048 на доске.
     Если да, возращвает значение True. В противном случае вернет значение False.
        """
    win = False
    for line in board:
        for num in line:
            if num == "2048":
                win = True
    return win


def add(board, i_list, j_list, i_direction, j_direction):
    """Выполняет итерацию по доске и добавляет число к соседнему соседу, если два числа совпадают.
     i_list, j_list - списки, указывающие, как добавление взаимодействует по списку.
     i_direction, j_direction - целое число, либо 1, -1, либо 0. Определяет направление добавления.
   ход - это счетчик, который позже используется для определения того, может ли игрок все еще сделать ход.
        """
    move = 0
    for i in i_list:
        for j in j_list:
            # проверяет, совпадают ли 2 числа, если да, складывает их вместе
            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i+ i_direction][j + j_direction] = str(int(board[i][j])+int(board[i+ i_direction][j+j_direction]))
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def push(board, i_list, j_list, i_direction, j_direction):
    """Вставляет число в соседнюю клетку, если клетка ровна 0.
     i_list, j_list - списки, указывающие, как push взаимодействует по списку.
     i_direction, j_direction - целое число, либо 1, -1, либо 0. Определяет направление толчка.
     ход - это счетчик, который позже используется для определения того, может ли игрок все еще сделать ход.
        """
    move = 0
    for i in i_list:
        for j in j_list:
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def pushDirection(board, UserInput):
    """Принимает пользовательский ввод и вызывает функцию добавления и нажатия с соответствующим i_list,
     j_list, i_direction и j_direction.
        """
    move = 0
    if UserInput == "u":
        i_list, j_list = range(1,4), range(4)
        i_direction, j_direction = -1, 0
    elif UserInput == "d":
        i_list, j_list = range(2,-1,-1), range(4)
        i_direction, j_direction = 1, 0
    elif UserInput == "l":
        i_list, j_list = range(4), range(1,4)
        i_direction, j_direction = 0, -1
    elif UserInput == "r":
        i_list, j_list = range(4), range(2,-1,-1)
        i_direction, j_direction = 0, 1
    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)
    move += add(board, i_list, j_list, i_direction, j_direction)
    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)

    return move


def checkCell(board, i, j):
    """
    Проверяет ячейку выше / ниже / слева / справа
    от доски[i][j] и проверяет, соответствует ли одна или несколько доск[i][j]
    , если да, вернет True.
     в противном случае вернет значение False.
        """
    move_i = []
    move_j = []
    board_size = len(board)
    if i > 0:
        move_i.append(-1)
        move_j.append(0)
    if i < (board_size - 1):
        move_i.append(1)
        move_j.append(0)
    if j > 0:
        move_j.append(-1)
        move_i.append(0)
    if j < (board_size - 1):
        move_j.append(1)
        move_i.append(0)
    for k in range(len(move_i)):
        if board[i + move_i[k]][j + move_j[k]] == board[i][j]:
            return True
    return False


def canMove(board):
    """Проверяет, может ли игрок все еще сделать ход.
     Если да, вернет значение True. В противном случае вернет значение False.
        """

    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                return True
            if checkCell(board, i, j):
                return True
    return False


def checkLose(board):
    """Проверяет доску, возвращает True,если в списке все еще есть 0 или
         есть еще какой-либо ход)
     в противном случае False
        """
    nozero = False
    for elt in board:
        nozero = nozero or ("0" in elt)

    if not nozero:
        return not canMove(board)
    return False


def main(board, UserInput):
    if not checkLose(board) and not checkWin(board):

        move = pushDirection(board, UserInput)
        if move != 0:
            addNewNum(board, 1)
    return board