import chess 
import numpy 
import numpy as np 
#heuristic function for chess (only accounts for pieces no king safety)
def heuristic_chess(board): 
    outcome = board.outcome()

    if outcome is not None: 
        winner = outcome.winner 
        termination = outcome.termination 
        if termination == chess.Termination.CHECKMATE: 
            if winner: 
                return 1 
            else: 
                return -1 
        else: 
            return 0 
    else: 
        wP = len(board.pieces(chess.PAWN, chess.WHITE))
        wN = len(board.pieces(chess.KNIGHT, chess.WHITE))
        wB = len(board.pieces(chess.BISHOP, chess.WHITE))
        wR = len(board.pieces(chess.ROOK, chess.WHITE))
        wQ = len(board.pieces(chess.QUEEN, chess.WHITE))

        bP = len(board.pieces(chess.PAWN, chess.BLACK))
        bN = len(board.pieces(chess.KNIGHT, chess.BLACK))
        bB = len(board.pieces(chess.BISHOP, chess.BLACK))
        bR = len(board.pieces(chess.ROOK, chess.BLACK))
        bQ = len(board.pieces(chess.QUEEN, chess.BLACK))

        fp = (wP - bP)
        fn = (wN - bN) 
        fb = (wB - bB)
        fR = (wR - bR) 
        fq = (wQ - bQ) 
        
        h_Value = fp + 3* fn + 4 * fb + 5 * fR + 9 * fq 
        h_Value = h_Value / 100 

        


        return h_Value 
    
#helper function to check wheather a limit has reached or not 
def is_cutoff(board, current_depth, depth_limit=2):
    outcome = board.outcome() 
    if outcome is not None: 
        return True
    elif current_depth == depth_limit: 
        return True 
    else: 
        return False 
    
#MinMax with heuristics and depth limit 
def h_minimax(board, depth_limit = 2):  
    return max_node(board, 0, depth_limit)
      


def max_node(board, current_depth, depth_limit):
    if is_cutoff(board,current_depth, depth_limit): 
        return heuristic_chess(board), None 
    v = - np.infty
    move = None 
    legal_moves = list(board.legal_moves)
    for a in legal_moves:
        board.push(a) 
        v2, a2 = min_node(board, current_depth + 1, depth_limit)
        board.pop()
        if v2 > v: 
            v, move = v2, a
    return v, move


def min_node(board, current_depth, depth_limit): 
    if is_cutoff(board, current_depth, depth_limit): 
        return heuristic_chess(board), None 
    v = np.infty
    move = None 
    moves = list(board.legal_moves)
    for a in moves: 
        board.push(a)
        v2, a2 = max_node(board, current_depth + 1, depth_limit) 
        board.pop()
        if v2 < v: 
            v, move = v2, a 
    return v, move 

#MinMax with alpha beta pruning + heuristic 
def h_minimax_alpha_beta(board, depth_limit = 2): 
    return max_node_ab(board, 0, depth_limit, -np.infty, np.infty)

def max_node_ab(board, current_depth, depth_limit, alpha, beta): 
    if is_cutoff(board,current_depth, depth_limit): 
        return heuristic_chess(board), None 
    v = - np.infty
    move = None 
    legal_moves = list(board.legal_moves)
    for a in legal_moves:
        board.push(a) 
        v2, a2 = min_node_ab(board, current_depth + 1, depth_limit, alpha, beta)
        board.pop()
        if v2 > v: 
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta: return v, move
    return v, move

def min_node_ab(board, current_depth, depth_limit, alpha, beta): 
    if is_cutoff(board, current_depth, depth_limit): 
        return heuristic_chess(board), None 
    v = np.infty
    move = None 
    moves = list(board.legal_moves)
    for a in moves: 
        board.push(a)
        v2, a2 = max_node_ab(board, current_depth + 1, depth_limit, alpha, beta) 
        board.pop()
        if v2 < v: 
            v, move = v2, a 
            beta = min(beta, v)
        if v <= alpha : return v, move
    return v, move 

        