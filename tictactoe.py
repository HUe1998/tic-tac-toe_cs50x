"""
Tic Tac Toe Player
"""
from collections import Counter
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    total_board = board[0] + board[1] + board[2]
    board_count = Counter(total_board)
    if board_count[X] > board_count[O]:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item is None:
                possible_actions.add((row_index, column_index))
    return possible_actions
    # Caution: any value is acceptable if terminal board is provided.


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise AttributeError('Invalid Action - placement already occupied')
    else:
        result_board = deepcopy(board)
        i, j = action
        result_board[i][j] = player(board)
        return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    total_board = board[0] + board[1] + board[2]

    # Possible Win Indexes in total_board
    win_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    x_index = set()
    o_index = set()
    for index, item in enumerate(total_board):
        if item == X:
            x_index.add(index)
        elif item == O:
            o_index.add(index)

    # Check whether indexes of X or O satisfy win condition
    for i in win_indexes:
        win_set = set(i)
        if win_set.issubset(x_index):
            return X
        elif win_set.issubset(o_index):
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    total_board = board[0] + board[1] + board[2]
    if None not in total_board:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_check = winner(board)
    if win_check is not None:
        if win_check == X:
            return 1
        else:
            return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            return max(actions(board), key=lambda a: min_value(result(board, a)))
        else:
            return min(actions(board), key=lambda a: max_value(result(board, a)))


# function Max-Value(state)
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


# function Min-Value(state)
def min_value(board):
    if terminal(board):
        return utility(board)
    w = math.inf
    for action in actions(board):
        w = min(w, max_value(result(board, action)))
    return w
