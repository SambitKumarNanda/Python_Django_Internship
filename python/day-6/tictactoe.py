import random

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

options = ['O','X']

def print_board():
    print(board[1], " | ",board[2]," | ",board[3]," | ")
    print("----","----","----","----")
    print(board[4], " | ",board[5]," | ",board[6]," | ")
    print("----","----","----","----")
    print(board[7], " | ",board[8]," | ",board[9]," | ")
    
    
player = options[random.randint(0, 1)]

def put_spot(key):
    board[key] = player
    
def player_swap(player):
    return 'X' if player1 == 'O' else 'O'


