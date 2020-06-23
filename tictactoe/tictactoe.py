"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
boards_log = []

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
    x = 0
    o = 0
    for l in board:
        for c in l:
            if c == 'X':
                x += 1
            elif c == 'O':
                o += 1
    return 'O' if o < x else 'X'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for idx_x, i in enumerate(board):
        for idx_y, j in enumerate(i):
            if j == None:
                actions.add((idx_x,idx_y))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action in actions(board):
        (i, j) = action
        result_board = copy.deepcopy(board)    
        result_board[i][j] = player(board)
        return result_board

    else:
        raise Exception("Invalid")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) and board[i][0] is not None:
            return 'X' if board[i][0] == X else 'O'
        if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]) and board[0][i] is not None:
            return 'X' if board[0][i] == X else 'O'

    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and board[1][1] is not None:
        return 'X' if board[1][1] == X else 'O'

    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and board[1][1] is not None:
        return 'X' if board[1][1] == X else 'O'

    for l in board:
        for c in l:
            if c == EMPTY:
                return None
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    result = winner(board)
    if result == X or result == O:
        return True
    else:
        for l in board:
            for c in l:
                if c == EMPTY:
                    return False

    return True    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if terminal(board):
        None

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))    #FIXED
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))    #FIXED
            if k < v:
                v = k
                best_move = action
    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v    #FIXED

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v    #FIXED

